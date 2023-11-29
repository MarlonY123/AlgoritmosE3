# %%
import networkx as nx
import matplotlib.pyplot as plt

# %%
G = nx.DiGraph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1, 3), (2,4), (3,4), (4, 5)])

# %%
'''
labels = {}
labels[1] = r"$a$"
labels[2] = r"$b$"
labels[3] = r"$c$"
labels[4] = r"$\alpha$"
labels[5] = r"$\beta$"
'''
pos = nx.spring_layout(G)
nx.draw(G, labels=dict([(n+1,n+1) for n in range(5)]))

# %%
['abc'] * 5
# %%
for n in G.nodes():
    print(n)
for (s,t) in G.edges():
    print(s,t)
for s in G.nodes():
    for t in G.successors(t):
        print(s, t)

# %%
print(list(G.predecessors(1)))

# %%
list(nx.dfs_edges(G))
# %%
G = nx.Graph()
G.add_edge(0,1,color='r',weight=2)
G.add_edge(1,2,weight=4)
G.add_edge(2,3,color='b',weight=6)
G.add_edge(3,4,color='y',weight=3)
G.add_edge(4,0,color='m',weight=1)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

colors = []
for e in G.edges():
    if e == (1,2):
        colors.append("blue")
    else:
        colors.append("black")

pos = nx.circular_layout(G)
nx.draw(G, pos, 
        edge_color=colors, 
        width=list([w*2 for w in weights]),
        with_labels=True,
        node_color='lightgreen')
# %%
colors
# %%
G = nx.DiGraph()
for i in range(5):
    G.add_edge(i, i + 1)
colors = []
for (src, tgt) in G.edges():
    if tgt % 2 == 0:
        colors.append("yellow")
    else:
        colors.append("black")
nx.draw(G, edge_color=colors)
# %%
g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)

nx.draw(g)
# %%
path = [(1,2), (2,4), (4,6)]
ncolors = []
for e in g.edges():
    if e in path:
        ncolors.append("red")
    else:
        ncolors.append("black")
nx.draw(g, edge_color=ncolors)

# %%