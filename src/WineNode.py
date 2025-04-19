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
        self.neighbors = {} #node: similarity score


    def createKeywords(self):
        keywords = set() #can use our R-B tree here too (i dont know if we doin that) COULD MAKE A CUSTOM TRIE TOO!!!
        for field in [self.description, self.title, self.winery, self.variety]:
            for word in field.split():
                clean = word.lower().strip(".,!?()[]{}\"'")
                if clean:
                    keywords.add(clean)
        return list(keywords)
    
    def similarityScore(self, other):
        #used this thing called jaccard similarity
        #can also use additional methods like cosine similarity and euclidean distance
        #could also use other features of wine for similarity on top of keywords
        intersection = len(set(self.keywords) & set(other.keywords))
        union = len(set(self.keywords) | set(other.keywords))
        if union == 0:
            return 0
        return intersection / union