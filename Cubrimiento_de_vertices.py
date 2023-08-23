
#!/usr/bin/python
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

#random.seed(30)


#Random graph with N vertices, with probability (0,1) to connect two given vertices
def generateRandomGraph(N,P):
    G=nx.gnp_random_graph(N,P)
    while (nx.is_connected(G)==False):
        G=nx.gnp_random_graph(N,P)

    best = 0
    total_aristas = G.number_of_edges()
    n_nodos = len(G.nodes())

    for option in range(1, 2**N):
        
        # Convertir el numero entero a binario en una lista de numpy
        vector = np.array([int(bit) for bit in str(bin(option)[2:]).zfill(N)])
        
        # Conjunto auxiliar: Aristas
        tmp = set() 

        # Conjunto auxiliar: Nodos
        tmp_2 = set() 

        # Vertices agregados
        Vertices_incluidos = np.where(vector == 1)[0]

        for vertice in Vertices_incluidos:

            # Consideracion para el vector inverso
            # En esta implementacion se tiene [...,3,2,1,0]
            # en lugar de [0,1,2,3,...] debido a los numeros binarios
            vertice = N - 1 - vertice  

            # Iteracion sobre las aristas del grafo
            for aristas in G.edges():

                if vertice in aristas:

                    # Agregar la arista 
                    tmp.add(aristas)

                    # Agregar el vertice
                    tmp_2.add(vertice)


        if len(tmp) == total_aristas and len(tmp_2) < n_nodos:
            best = np.copy(vector)
            n_nodos = len(tmp_2)
            
    print(best)

    return G
    

if __name__ == '__main__':
    G=generateRandomGraph(6,0.1)
    nx.draw(G,with_labels="true")
    plt.show()

        