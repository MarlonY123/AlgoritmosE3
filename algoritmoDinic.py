import networkx as nx
import matplotlib.pyplot as plt

def BFS(s, t,graph,levels):
        levels[s] = 0
        queue = []
        queue.append(s)
        while queue:
            u = queue.pop(0)
            for i in graph[u]:
                e = graph[u][i]
                if levels[i] < 0 and e['flow'] < e['capacity']:
                    levels[i] = levels[u]+1
                    queue.append(i)
        return False if levels[t] < 0 else True
def sendFlow(graph, u, flow, t, start,levels):
    if u == t:
        return flow

    # Traverse all adjacent edges one -by -one
    #while start[u] < len(graph[u]):
    for v in graph[u]:
        # Pick next edge from adjacency list of u
        e = graph[u][v]
        if levels[v] == levels[u]+1 and e['flow'] < e['capacity']:
            # find minimum flow from u to t
            curr_flow = min(flow, e['capacity']-e['flow'])
            temp_flow = sendFlow(graph,v, curr_flow, t, start,levels)

            # flow is greater than zero
            if temp_flow and temp_flow > 0:

                # add flow to current edge
                e['flow'] += temp_flow

                # subtract flow from reverse edge
                # of current edge
                #adj[e.v][e.rev].flow -= temp_flow
                print(v)
                print(graph[v])
                graph[v][len(graph[v])] -= temp_flow
                return temp_flow
        #start[u] += 1
# Returns maximum flow in graph
def DinicMaxflow(s, t,graph):
    levels = [-1]*(max(G) + 1)
    # Corner case
    if s == t:
        return -1

    # Initialize result
    total = 0

    # Augument the flow while there is path
    # from source to sink
    while BFS(s, t,graph,levels):

        # store how many edges are visited
        # from V { 0 to V }
        #start = [0 for i in range(max(graph)+1)]
        start = 0
        #print(start)
        while True:
            flow = sendFlow(graph,s, float('inf'), t, start,levels)
            if not flow:
                break

            # Add path flow to overall flow
            total += flow

    # return maximum flow
    return total
 

G = nx.DiGraph()
s,t = 0,10
G.add_nodes_from([s,1,2,3,4,5,6,7,8,9,t])
G.add_weighted_edges_from([(0,1,5), (0,2,10), (0,3,15), (1,0,0), (2,0,0),(3,0,0),
                           (1,4,10),(1,2,0),(4,1,0),(2,1,15),(2,5,20),(5,2,0),(3,5,0),
                           (5,3,5),(3,6,25),(6,3,0),(5,4,0),(4,5,25),(4,7,10),(7,4,0),
                           (5,8,30),(8,5,0),(6,8,20),(8,6,0),(6,9,10),(9,6,0),(4,8,0),
                           ( 8,4,15),(7,10,5),(10,7,0),(8,10,15),(10,8,0),(8,9,15),(9,8,0),
                           (9,10,10),(10,9,0)])
for u, v, attrs in G.edges(data=True):
    G[u][v]['flow'] = 0
    if 'weight' in attrs:
        attrs['capacity'] = attrs.pop('weight')
#max_flow_value = nx.maximum_flow_value(G, s, t)
#print(max_flow_value)
print(DinicMaxflow(s,t,G))
#print(len(G[0]))