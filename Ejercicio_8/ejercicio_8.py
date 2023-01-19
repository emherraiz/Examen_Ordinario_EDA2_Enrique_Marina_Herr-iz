import networkx as nx
import itertools

def main():
    # Crear el grafo
    G = nx.Graph()

    # Agregar los planetas como nodos
    planets = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'planeta1', 'planeta2', 'planeta3', 'planeta4', 'planeta5', 'planeta6', 'planeta7']
    G.add_nodes_from(planets)

    # Crear una lista de tuplas con las relaciones entre los planetas y con un peso asociado
    planet_pairs = list(itertools.combinations(planets, 2))
    for i, pair in enumerate(planet_pairs):
        G.add_edge(pair[0], pair[1], weight=i)


    # Encontrar el árbol de expansión mínima utilizando el algoritmo de Prim
    T = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
    print(T.edges())



    # Encontrar el camino más corto entre Tatooine y Dagobah
    path1 = nx.shortest_path(G, 'Tatooine', 'Dagobah', weight='weight')
    print("Shortest path from Tatooine to Dagobah:", path1)

    # Encontrar el camino más corto entre Alderaan y Endor
    path2 = nx.shortest_path(G, 'Alderaan', 'Endor', weight='weight')
    print("Shortest path from Alderaan to Endor:", path2)

    # Encontrar el camino más corto entre Hoth y Tatooine
    path3 = nx.shortest_path(G, 'Hoth', 'Tatooine', weight='weight')
    print("Shortest path from Hoth to Tatooine:", path3)


    # Encontrar todos los planetas a los que se puede llegar desde Tatooine
    successors = nx.bfs_successors(G, 'Tatooine')
    print("All planets reachable from Tatooine:", list(successors))



if __name__ == "__main__":
    main()
