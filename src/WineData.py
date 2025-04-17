### Cleaning and Preparing the Data from Kaggle Repo

### Link to Data Set: https://www.kaggle.com/datasets/zynicide/wine-reviews?resource=download


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Read in (130k columns)
wine_data = pd.read_csv('DATA/winemag-data-130k-v2.csv')

### Only care about Name,Country,Price,Wine Score

## Should we keep description so we can return the description to user after found related wine???
## Now thinking about it could be useful to keep a lot of this information to return to user once reccomendation is found
## Could have 2 dataframes - one for sorting and then we could create a map to find the other values we care about - would be more efficient

### wine_data = wine_data.drop(columns = ['province', ''], inplace = True)




