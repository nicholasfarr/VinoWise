from WineData import load_wine_nodes

def main():
    wine_nodes = load_wine_nodes()
    #testing that they work and printing out 5 of em
    print(f"Loaded {len(wine_nodes)} wine nodes.")

    for node in list(wine_nodes)[:5]:
        print(f"Wine ID: {node.id}, Name: {node.title}, Points: {node.points}, Price: {node.price}")

if __name__ == "__main__":
    main()