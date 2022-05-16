import networkx as nx
from stack_graph_depth_first_search_graphs import Stack
from Queue_explanation import Queue
from max_binary_heap import PQ

G = nx.Graph()
G.add_node('A2')
G.add_nodes_from(['A3', 'A4', 'A5'])

G.add_edge('A2', 'A3')
G.add_edges_from([('A3', 'A4'), ('A4', 'A5')])

for i in range(2, 6):
    G.add_edge('B{}'.format(i), 'C{}'.format(i))
    if 2 < i < 5:
        G.add_edge('B{}'.format(i), 'B{}'.format(i+1))
    if i < 5:
        G.add_edge('C{}'.format(i), 'C{}'.format(i+1))


maze = nx.Graph()

maze.add_edges_from([('0,0', '0,1'), ('0,0', '1,0'), ('0,1', '0,2'),
                    ('0,2', '1,2'), ('0,2', '0,3'), ('0,3', '1,3'), ('0,3', '0,4')])
maze.add_edges_from([('1,0', '1,1'), ('1,0', '2,0'), ('0,4', '1,4'),
                    ('1,2', '2,2'), ('1,4', '2,4'), ('1,1', '2,1'), ('2,1', '2,2')])
maze.add_edges_from([('2,2', '2,3'), ('2,3', '2,4')])


def path_to(node_from, src, target):
    if not target in node_from:
        raise ValueError('Unreachable')

    path = []
    v = target
    while v != src:
        path.append(v)
        v = node_from[v]

    path.append(src)
    path.reverse()
    return path


def dfs_search(G, src):
    marked = {}
    node_from = {}

    stack = Stack()
    marked[src] = True
    stack.push(src)

    while not stack.is_empty():
        v = stack.pop()
        for w in G[v]:
            if not w in marked:
                node_from[w] = v
                marked[w] = True
                stack.push(w)

    return node_from


def dfs_search_recursive(G, src):
    marked = {}
    node_from = {}

    def dfs(v):
        marked[v] = True
        for w in G[v]:
            if not w in marked:
                node_from[w] = v
                dfs(w)

    dfs(src)
    return node_from


"""
node_from = dfs_search(maze, '0,2')
print(path_to(node_from, '0,2', '2,2'))
"""


def bfs_search(G, src):
    marked = {}
    node_from = {}

    q = Queue()
    marked[src] = True
    q.enqueue(src)

    while not q.is_empty():
        v = q.dequeue()
        for w in G[v]:
            if not w in marked:
                node_from[w] = v
                marked[w] = True
                q.enqueue(w)

    return node_from


"""
node_from = bfs_search(maze, '0,2')
print(path_to(node_from, '0,2', '2,2'))
"""


def guided_search(G, src, target):
    marked = {}
    node_from = {}

    pq = PQ(G.number_of_nodes())
    marked[src] = True
    pq.enqueue(src, -distance_to(src, target))

    while not pq.is_empty():
        v = pq.dequeue()

        for w in G.neighbors(v):
            if not w in marked:
                node_from[w] = v
                marked[w] = True
                pq.enqueue(w, -distance_to(w, target))

    return node_from


def distance_to(from_cell, to_cell):
    return abs(from_cell[0] - to_cell[0]) + abs(from_cell[1] - to_cell[1])


def has_cycle(DG):
    marked = {}
    in_stack = {}

    def dfs(v):
        in_stack[v] = True
        marked[v] = True

        for w in DG[v]:
            if not w in marked:
                if dfs(w):
                    return True
            else:
                if w in in_stack and in_stack[w]:
                    return True

        in_stack[v] = False
        return False

    for v in DG.nodes():
        if not v in marked:
            if dfs(v):
                return True
    return False


def topological_sort(DG):
    marked = {}
    postorder = []

    def dfs(v):
        marked[v] = True
        for w in DG[v]:
            if not w in marked:
                dfs(w)
        postorder.append(v)

    for v in DG.nodes():
        if not v in marked:
            dfs(v)

    return reversed(postorder)


"""
print(list(G))
print(G.number_of_nodes(), 'nodes.')
print(G.number_of_edges(), 'edges.')
print('adjacent nodes to C3:', list(G['C3']))
print('adjacent nodes to C4:', list(G['C4']))
print('edges adjacent to C4:', list(G.edges('C4')))

12 nodes.
12 edges.
adjacent nodes to C3: ['C2', 'B3', 'C4']
edges adjacent to C3: [('C3', 'C2'), ('C3', 'B3'), ('C3', 'C4')]
"""
