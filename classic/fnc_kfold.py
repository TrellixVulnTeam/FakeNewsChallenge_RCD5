import sys
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from feature_engineering import refuting_features, polarity_features, hand_features, word_overlap_features
from feature_engineering import clean, get_tokenized_lemmas, gen_or_load_feats
from utils.dataset import DataSet
from utils.generate_test_splits import kfold_split, get_stances_for_folds
from utils.score import print_confusion_matrix, LABELS, score_submission, report_score

from utils.system import parse_params, check_version


def generate_features(stances,dataset,name):
    h, b, y = [],[],[]

    for stance in stances:
        y.append(LABELS.index(stance['Stance']))
        h.append(stance['Headline'])
        b.append(dataset.articles[stance['Body ID']])

    print("Cleaning text")
    clean_headlines = list(map(clean, h))
    clean_bodies = list(map(clean, b))
    print("Lemmatizing text")
    clean_lemmatized_headlines = list(map(get_tokenized_lemmas, clean_headlines))
    clean_lemmatized_bodies = list(map(get_tokenized_lemmas, clean_bodies))

    X_overlap = gen_or_load_feats(word_overlap_features,
        clean_lemmatized_headlines, clean_lemmatized_bodies, "features/overlap."+name+".npy")
    X_refuting = gen_or_load_feats(refuting_features,
        clean_lemmatized_headlines, clean_lemmatized_bodies, "features/refuting."+name+".npy")
    X_polarity = gen_or_load_feats(polarity_features,
        clean_lemmatized_headlines, clean_lemmatized_bodies, "features/polarity."+name+".npy")
    X_hand = gen_or_load_feats(hand_features, clean_headlines, clean_bodies, "features/hand."+name+".npy")

    X = np.c_[X_hand, X_polarity, X_refuting, X_overlap]
    return X,y


if __name__ == "__main__":
    check_version()
    parse_params()

    d = DataSet()
    folds,hold_out = kfold_split(d,n_folds=10)
    fold_stances, hold_out_stances = get_stances_for_folds(d,folds,hold_out)

    Xs = dict()
    ys = dict()

    # Load/Precompute all features now
    print("Computing features for holdout")
    X_holdout,y_holdout = generate_features(hold_out_stances,d,"holdout")
    for fold in fold_stances:
        print("Computing features for fold "+ str(fold))
        Xs[fold],ys[fold] = generate_features(fold_stances[fold],d,str(fold))

    best_score = 0
    best_fold = None
    cm = None

    average_score = 0
    total_count = 0

    print("Classifying folds")

    # Classifier for each fold
    for fold in fold_stances:
        ids = list(range(len(folds)))
        del ids[fold]

        X_train = np.vstack(tuple([Xs[i] for i in ids]))
        y_train = np.hstack(tuple([ys[i] for i in ids]))

        X_test = Xs[fold]
        y_test = ys[fold]

        clf = GradientBoostingClassifier(n_estimators=200, random_state=14128, verbose=True)
        clf.fit(X_train, y_train)

        predicted = [LABELS[int(a)] for a in clf.predict(X_test)]
        actual = [LABELS[int(a)] for a in y_test]

        fold_score, cm = score_submission(actual, predicted)
        max_fold_score, _ = score_submission(actual, actual)

        score = fold_score/max_fold_score
        average_score += score

        print("Score for fold "+ str(fold) + " - " + str(score))
        if score > best_score:
            best_score = score
            best_fold = clf
            best_cm = cm

    average_score /= len(fold_stances)

    print("Best score " + str(best_score))
    print("Confusion matrix for best:")
    print_confusion_matrix(best_cm)

    print("Average score " + str(average_score))

    print("Classifying holdout")
    #Run on Holdout set and report the final score on the holdout set
    predicted = [LABELS[int(a)] for a in best_fold.predict(X_holdout)]
    actual = [LABELS[int(a)] for a in y_holdout]

    report_score(actual,predicted)
