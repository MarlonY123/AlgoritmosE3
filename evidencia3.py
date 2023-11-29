# %%
import networkx as nx
import matplotlib.pyplot as plt

# %%
def BFS_levels(graph, s,levels):
    remover = []
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
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                levels[i] = levels[s] + 1
            else:
                if(levels[s] > levels[i]):
                    remover.append([s,i])
    #Modificar para arreglar que se remuevan todos los nodos innecesarios
    for i in remover:
        graph.remove_edge(i[0],i[1])
# %%
G = nx.DiGraph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10])
G.add_weighted_edges_from([(0,1,5), (0,2,10), (0,3,15), (1,0,-5), (2,0,-10),(3,0,-15),(1,4,10),(1,2,0),(4,1,-5),(2,1,15),(2,5,20),(5,2,-10),(3,5,),(5,3),(3,6),(6,3),(5,4),(4,5),(4,7),(7,4),(5,8),(8,5),(6,8),(8,6),(6,9),(9,6),(4,8),(8,4),(7,10),(10,7),(8,10),(10,8),(8,9),(9,8),(9,10),(10,9)])
pos = nx.spring_layout(G)
nx.draw(G, pos,labels=dict([(n,n) for n in range(11)]))  
print(list(G.successors(0)))
# %% 
#levels = {}
#BFS_levels(G,0,levels)
#nx.draw(G, pos,labels=levels)  
#print(levels)
    # %%
