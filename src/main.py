from WineData import *

def main():
    wine_nodes = load_wine_nodes()
    #testing that they work and printing out 5 of em
    print(f"Loaded {len(wine_nodes)} wine nodes.")

    node = findWineByName(wine_nodes, "Tandem 2011 Ars In Vitro Tempranillo-Merlot (Navarra)")
    if node:
        print(f"Wine ID: {node.id}, Name: {node.title}, Points: {node.points}, Price: {node.price}")
        createSimilarityScoreDict(wine_nodes, node)
        print(f"Similarity scores for {node.title}:")
        for neighbor, score in node.neighbors.items():
            print(f"Neighbor: {neighbor.title}, Similarity Score: {score}")
        

if __name__ == "__main__":
    main()