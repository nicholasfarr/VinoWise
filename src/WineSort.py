from sorts import *
import time

def findRecommendationsMerge(node, amount: int):
    start = time.perf_counter()
    sorted_items = merge_sort(list(node.neighbors.items()))
    elapsed = time.perf_counter() - start
    return sorted_items[:amount], elapsed


def findRecommendationsQuick(node, amount: int):
    start = time.perf_counter()
    sorted_items = quick_sort(list(node.neighbors.items()))
    elapsed = time.perf_counter() - start
    return sorted_items[:amount], elapsed

#probably should have a function to find the best wine for a user based on their preferences
#also have a way for user to test between quick sort and merge sort and return the time it takes


# def findBestWine(wine_nodes, user_preferences):
