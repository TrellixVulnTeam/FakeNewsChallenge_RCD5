from csv import DictReader


class DataSet():
    def __init__(self, prefix="train", path="../datasets"):
        self.path = path

        print("Reading dataset")
        bodies = prefix + "_bodies.csv"
        stances = prefix + "_stances.csv"

        self.stances = self.read(stances)
        articles = self.read(bodies)
        self.articles = dict()

        #make the body ID an integer value
        for s in self.stances:
            s['Body ID'] = int(s['Body ID'])

        #copy all bodies into a dictionary
        for article in articles:
            self.articles[int(article['Body ID'])] = article['articleBody']

        print("Total " + prefix + " stances: " + str(len(self.stances)))
        print("Total " + prefix + " bodies: " + str(len(self.articles)))



    def read(self,filename):
        rows = []
        with open(self.path + "/" + filename, "r", encoding='utf-8') as table:
            r = DictReader(table)

            for line in r:
                rows.append(line)
        return rows
