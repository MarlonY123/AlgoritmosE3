# %%
import networkx as nx
import matplotlib.pyplot as plt

# %%
def BFS_levels(graph, s,levels,t):
    visited = [False] * (max(graph) + 1)
    queue = []
    queue.append(s)
    visited[s] = True
    levels[s] = 0

    while queue:
        s = queue.pop(0)
        #print(s, end=" ")
        #print('Origen: ',s,' Nodos conectados: ', graph[s])
        for i in graph[s]:
            capacidad = graph[s][i]['weight']
            if visited[i] == False and  capacidad > 0:
                print("De ", s," a: ", i ," capacidad:",graph[s][i]['weight'])
                queue.append(i)
                visited[i] = True
                levels[i] = levels[s] + 1
    return visited[t] != False
# %%
G = nx.DiGraph()
s,t = 0,10
G.add_nodes_from([s,1,2,3,4,5,6,7,8,9,t])
G.add_weighted_edges_from([(0,1,5), (0,2,10), (0,3,15), (1,0,0), (2,0,0),(3,0,0),
                           (1,4,10),(1,2,0),(4,1,0),(2,1,15),(2,5,20),(5,2,0),(3,5,0),
                           (5,3,5),(3,6,25),(6,3,0),(5,4,0),(4,5,25),(4,7,10),(7,4,0),
                           (5,8,30),(8,5,0),(6,8,20),(8,6,0),(6,9,10),(9,6,0),(4,8,0),
                           (8,4,15),(7,10,5),(10,7,0),(8,10,15),(10,8,0),(8,9,15),(9,8,0),
                           (9,10,10),(10,9,0)])

pos = nx.spring_layout(G)
nx.draw(G, pos,labels=dict([(n,n) for n in range(11)]))  
# %% 
levels = {}
print(BFS_levels(G,s,levels,t))
nx.draw(G, pos,labels=levels)  
print(levels)
    # %%
