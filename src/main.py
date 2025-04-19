from WineData import *

def main():
    wine_nodes = load_wine_nodes()
    #testing that they work and printing out 5 of em
    print(f"Loaded {len(wine_nodes)} wine nodes.")

    node = findWineByName(wine_nodes, "Tandem 2011 Ars In Vitro Tempranillo-Merlot (Navarra)")
    if node:
        print(f"Wine ID: {node.id}, Name: {node.title}, Points: {node.points}, Price: {node.price}")

if __name__ == "__main__":
    main()