from sorts import *

def findRecommendationsMerge(node, amount: int):    
        
    sorted_items = merge_sort(list(node.neighbors.items()))
    return [key for key, _ in sorted_items[:amount]]

def findRecommendationsQuick(node, amount: int):
    sorted_items = quick_sort(list(node.neighbors.items()))
    return [key for key, _ in sorted_items[:amount]]

#probably should have a function to find the best wine for a user based on their preferences
#also have a way for user to test between quick sort and merge sort and return the time it takes


# def findBestWine(wine_nodes, user_preferences):
