import networkx as nx
from IndexedMinPQ import IndexedMinPQ


def dijkstra_sp(G, src):
    N = G.number_of_nodes()

    inf = float('inf')
    dist_to = {v: inf for v in G.nodes()}
    dist_to[src] = 0

    impq = IndexedMinPQ(N)
    impq.enqueue(src, dist_to[src])
    for v in G.nodes():
        if v != src:
            impq.enqueue(v, inf)

    def relax(e):
        n, v, weight = e[0], e[1], e[2]["WEIGHT"]
        if dist_to[n] + weight < dist_to[v]:
            dist_to[v] = dist_to[n] + weight
            edge_to[v] = e
            impq.decrease_priority(v, dist_to[v])

    edge_to = {}
    while not impq.is_empty():
        n = impq.dequeue()
        for e in G.edges(n, data=True):
            relax(e)

    return (dist_to, edge_to)


def edges_path_to(edge_to, src, target):
    if not target in edge_to:
        raise ValueError('Unreachable')

    path = []
    v = target
    while v != src:
        path.append(v)
        v = edge_to[v][0]

    path.append(src)
    path.reverse()
    return path


G = nx.DiGraph()
G.add_edges_from([('a', 'b', {"WEIGHT": 6}), ('a', 'c', {
                 "WEIGHT": 10}), ('b', 'c', {"WEIGHT": 2})])

dist_to, edge_to = dijkstra_sp(G, 'a')
print(edges_path_to(edge_to, 'a', 'c'))
