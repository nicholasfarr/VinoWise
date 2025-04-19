class WineNode:
    def __init__(self, wine_id, variety, country, province, region_1,
                 price, points, description, winery, title):
        self.id = wine_id #could just randomly generate a ID here.
        self.variety = variety
        self.country = country
        self.province = province
        self.region_1 = region_1
        self.price = price
        self.points = points
        self.description = description
        self.winery = winery
        self.title = title

        self.keywords = self.createKeywords()  #to make a similarity score
        self.similarity_score = 0.0

    def createKeywords(self):
        keywords = set() #can use our R-B tree here too
        for field in [self.description, self.title, self.winery, self.variety]:
            for word in field.split():
                clean = word.lower().strip(".,!?()[]{}\"'")
                if clean:
                    keywords.add(clean)
        return list(keywords)