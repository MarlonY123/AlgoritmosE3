# %%
import networkx as nx
import matplotlib.pyplot as plt

# %%
def BFS(graph, s,levels):

    visited = [False] * (max(graph) + 1)
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
 
# %%
G = nx.DiGraph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10])
G.add_edges_from([(0,1), (0,2), (0,3), (1,0), (2,0),(3,0),(1,4),(1,2),(4,1),(2,1),(2,5),(5,2),(3,5),(5,3),(3,6),(6,3),(5,4),(4,5),(4,7),(7,4),(5,8),(8,5),(6,8),(8,6),(6,9),(9,6),(4,8),(8,4),(7,10),(10,7),(8,10),(10,8),(8,9),(9,8),(9,10),(10,9)])
#pos = nx.spring_layout(G)
#nx.draw(G, pos,labels=dict([(n,n) for n in range(11)]))   
levels = {}
BFS(G,0,levels)
    # %%
