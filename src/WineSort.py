from sorts import *

def findRecommendationsMerge(node, amount: int):        
    sorted_items = merge_sort(node.neighbors)
    return [key for key, _ in sorted_items[:amount]]

def findRecommendationsQuick(node, amount: int):
    sorted_items = quick_sort(node.neighbors)
    return [key for key, _ in sorted_items[:amount]]    


def SortWineScore():
    return 10
