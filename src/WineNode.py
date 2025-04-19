class WineNode:
    def __init__(self, wine_id, variety, country,
                 price, points, description, winery, title):
        self.id = wine_id #could just randomly generate a ID here.
        self.variety = variety
        self.country = country
        self.description = description
        self.winery = winery
        self.title = title
        self.points = points #could also let the user see top 100 rated wines or something
        self.price = price
        self.keywords = self.createKeywords()  #to make a similarity score
        self.similarity_score = 0.0

    def createKeywords(self):
        keywords = set() #can use our R-B tree here too (i dont know if we doin that) COULD MAKE A CUSTOM TRIE TOO!!!
        for field in [self.description, self.title, self.winery, self.variety]:
            for word in field.split():
                clean = word.lower().strip(".,!?()[]{}\"'")
                if clean:
                    keywords.add(clean)
        return list(keywords)