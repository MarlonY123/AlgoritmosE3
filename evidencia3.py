#%%
import networkx as nx
import matplotlib.pyplot as plt
import os
from collections import deque

#%%
#Clase que crea las aristas
class Edge:
    def __init__(self, v, flujo, C, rev):
        self.v = v #Nodo destino
        self.flujo = flujo #Flujo
        self.C = C #Capacidad 
        self.rev = rev #Índice de la arista inversa
#Clase que crea los grafos
class Graph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0 for i in range(V)]
    #Metodo para agregar aristas a los vertices del grafo
    def addEdge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)

    #Metodo para realizar el Breadth First Search
    #Complejidad temporal O(V+E)
    #En donde V son la cantidad de vertices y E la de aristas
    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1

        self.level[s] = 0
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flujo < e.C:

                    self.level[e.v] = self.level[u] + 1
                    q.append(e.v)

        return False if self.level[t] < 0 else True
    #Método que manda flow a todos las edges para comprobar la capacidad de ese camino, es una modificación del algortimo del DFS
    #Complejidad O(V * E^2), 
    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow
        while start[u] < len(self.adj[u]):

            e = self.adj[u][start[u]]
            if self.level[e.v] == self.level[u] + 1 and e.flujo < e.C:
                curr_flow = min(flow, e.C - e.flujo)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
                if temp_flow and temp_flow > 0:
                    e.flujo += temp_flow
                    self.adj[e.v][e.rev].flujo -= temp_flow
                    return temp_flow
            start[u] += 1
    #Método que regresa el maximum flow de todo el grafo mediante la implementación del BFS y el DFS modificado
    #Complejidad temporal de O(V^2 * E)
    def DinicMaxflow(self, s, t):
        if s == t:
            return -1
        total = 0
        while self.BFS(s, t):
            start = [0 for i in range(self.V + 1)]
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
                total += flow
        return total


#%%
#Abrir archivo de texto y crear el origen, destino, numero de aristas y aristas
def readFile(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    origen, destino, aristasNum = map(int, lines[0].split())
    aristas = [list(map(int, line.split())) for line in lines[1:]]

    return origen, destino, aristasNum, aristas

#%%
#Mostrar grafo con nx.draw, modificando los colores de acuerdo al nivel
def printGrafo(g, levels, path=[], title='', pos=None):
    plt.title(title)
    nodeColor = list(levels.values())
    pathColor = 'green'

    if pos is None:
        pos = nx.spring_layout(g)

    nx.draw(g, pos, with_labels=True, node_color=nodeColor, cmap=plt.cm.YlGnBu)

    if path:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color=pathColor, width=2)

    plt.show()
    return pos

#%%Z
def printDinic(g_networkx,g_dinic, start, pos):
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            pos = printGrafo(g_networkx, bfslevels(g_dinic, start), path=list(visited),
                                  title=f'Recorrido(DFS) {current}', pos=pos)
            stack.extend(neighbor for neighbor in g_networkx.neighbors(current) if neighbor not in visited)
    return pos

#%%
#Método que realiza un BFS por todo el grafo para poder obtener los niveles de cada nodo según
#su capacidad y posición, además que serán usados como etiquetas para la visualización
#Complejidad temporal de O(V + E).
def bfslevels(g, source):
    levels = {}
    queue = deque([(source, 0)])

    while queue:
        curr, lvl = queue.popleft()

        if curr not in levels:
            levels[curr] = lvl

            for neighbor in g.adj[curr]:
                queue.append((neighbor.v, lvl + 1))

    return levels

#%%
#Función principal donde se hace uso de la lectura de archivo, algoritmo de Dinic y visualización de grafos
def main():
    file_path = "Grafo/grafo3.txt"
    origen, destino, aristasNum, aristas = readFile(file_path)

    #Se crean los grafos para el algoritmo de Dinic y su visualizacion
    visG = nx.DiGraph()
    dinicG = Graph(max(max(edge[0], edge[1]) for edge in aristas) + 1)
    for edge in aristas:
        dinicG.addEdge(edge[0], edge[1], edge[2])

    # Agregar nodos y aristas al grafo de visualizacion
    for edge in aristas:
        visG.add_edge(edge[0], edge[1])

    # DIBUJADO DEL GRAFO ANTES DEL ALGORITMO DE DINIC
    pos_networkx = nx.spring_layout(visG)
    pos_networkx = printGrafo(visG, {}, title='Grafo Original', pos=pos_networkx)
    
    #DIBUJADO DEL GRAFO DESPUES DEL ALGORITMO DE DINIC
    levels_dinic = bfslevels(dinicG, origen) #BFS
    pos_networkx = printGrafo(visG, levels_dinic, title='Grafo con Dinic', pos=pos_networkx)
    pos_networkx = printDinic(visG, dinicG, origen, pos_networkx)
    flujoMax = dinicG.DinicMaxflow(origen, destino)
    print("Niveles de Dinic:", levels_dinic)
    print("Flujo maximo:", flujoMax)
    print("Numero de aristas:", aristasNum)
#%%
main()