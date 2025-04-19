
# Link to Data Set: https://www.kaggle.com/datasets/zynicide/wine-reviews?resource=download

import pandas as pd 
from WineNode import WineNode 
import os

## Read in (130k columns)

### Only care about Name,Country,Price,Wine Score

## Should we keep description so we can return the description to user after found related wine???
## Now thinking about it could be useful to keep a lot of this information to return to user once reccomendation is found
## Could have 2 dataframes - one for sorting and then we could create a map to find the other values we care about - would be more efficient

### wine_data = wine_data.drop(columns = ['province', ''], inplace = True)

def load_wine_nodes():
    base_path = os.path.dirname(__file__)  # Gets the path of WineData.py
    csv_path = os.path.join(base_path, '..', 'DATA', 'winemag-data-130k-v2.csv')
    csv_path = os.path.abspath(csv_path)  # Converts to full path

    pandasData = pd.read_csv(csv_path)

    #drop nodes without theses values
    pandasData = pandasData.dropna(subset=["country", "description", "points", "price", "title", "variety", "winery"])

    wine_nodes = []

    for i, row in pandasData.iterrows():
        try:
            node = WineNode(
                wine_id=i,  #miight not be needed imo
                variety=row["variety"],
                country=row["country"],
                price=float(row["price"]),
                points=int(row["points"]),
                description=row["description"],
                winery=row["winery"],
                title=row["title"]
            )
            wine_nodes.append(node)
        except Exception as e:
            print(f"Error at row {i}: {e}")
            continue

    return wine_nodes


def findWineByName(wine_nodes, title):
    for node in wine_nodes:
        if node.title == title:
            return node
    raise NameError(f"Wine with title '{title}' not found.")

def createSimilarityScoreDict(wine_nodes, node):
    for other_node in wine_nodes:
        if node.id != other_node.id:
            score = node.similarityScore(other_node)
            node.neighbors[other_node] = score
