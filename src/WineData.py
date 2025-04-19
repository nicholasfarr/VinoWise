
# Link to Data Set: https://www.kaggle.com/datasets/zynicide/wine-reviews?resource=download

import pandas as pd 
from WineNode import WineNode 

## Read in (130k columns)

### Only care about Name,Country,Price,Wine Score

## Should we keep description so we can return the description to user after found related wine???
## Now thinking about it could be useful to keep a lot of this information to return to user once reccomendation is found
## Could have 2 dataframes - one for sorting and then we could create a map to find the other values we care about - would be more efficient

### wine_data = wine_data.drop(columns = ['province', ''], inplace = True)

def load_wine_nodes():
    filepath = 'DATA/winemag-data-130k-v2.csv'

    pandasData = pd.read_csv(filepath)

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


