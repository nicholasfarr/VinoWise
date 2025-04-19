from WineData import *
from WineSort import *

def main():
    wine_nodes = load_wine_nodes()
    #testing that they work and printing out 5 of em
    print(f"Loaded {len(wine_nodes)} wine nodes.")

    node = findWineByName(wine_nodes, "Tandem 2011 Ars In Vitro Tempranillo-Merlot (Navarra)")
    if node:
        print(f"Wine ID: {node.id}, Name: {node.title}, Points: {node.points}, Price: {node.price}")
        createSimilarityScoreDict(wine_nodes, node)
        print(f"Similarity scores for {node.title}:")
        tup = findRecommendationsQuick(node, 5)
        for neighbor, score in tup[0]:
            print(f"Neighbor: {neighbor.title}, Similarity Score: {score}")
        print(f"Time taken for quick sort: {tup[1]} seconds")
        tup2 = findRecommendationsMerge(node, 5)
        for neighbor, score in tup2[0]:
            print(f"Neighbor: {neighbor.title}, Similarity Score: {score}")
        print(f"Time taken for merge sort: {tup2[1]} seconds")
        print(f"Difference: {tup[1] - tup2[1]} seconds")

if __name__ == "__main__":
    main()