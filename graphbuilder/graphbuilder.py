"""Provide the primary functions."""


import networkx as nx

def build_graph1():
    G = nx.Graph()
    G.add_nodes_from([i for i in range(10)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(10)])
    G.add_edge(2,5)
    G.add_edge(4,8)
    G.add_edge(4,0)
    for e in G.edges:
        G.edges[e]['weight'] = 1.0

    return G
    
def build_graph2():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    return G

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    pass
