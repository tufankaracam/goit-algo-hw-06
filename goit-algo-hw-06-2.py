# Task 2
import networkx as nx

G = nx.Graph()

edges = [
    ("Bus Terminal", "University"),
    ("University", "Library"),
    ("Library", "Shopping Mall"),
    ("Shopping Mall", "Stadium"),
    ("Stadium", "Airport"),
    ("Airport", "Museum"),
    ("Museum", "Bus Terminal"),
    ("Shopping Mall", "Hospital"),
    ("Hospital", "Cinema"),
    ("Cinema", "Bus Terminal"),
    ("University", "Cafe"),
    ("Cafe", "Airport"),
    ("Cinema", "Stadium"),
    ("Museum", "University"),
    ("Hospital", "Stadium"),
]

G.add_edges_from(edges)
graph = {vertex: set([t for t in G.neighbors(vertex)]) for vertex in G}


def dfs_paths(graph, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)
    return path


def bfs_paths(graph, start):
    visited = set()
    queue = [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(graph[vertex] - visited)
    return path


dfs_path = dfs_paths(graph, 'University')
bfs_path = bfs_paths(graph, 'University')

print(dfs_path)
print(bfs_path)

"""
Depth-First Search (DFS) and Breadth-First Search (BFS) are algorithms that traverse or search a graph or network and determine how one can reach other nodes from a particular starting node.

DFS prefers to go deeper into the graph by exploring from the first node it discovers, then it backtracks, whereas BFS aims to visit all nodes at the same level (i.e., equally distant from the starting node) first.

We can see these properties from their outputs.

DFS output: In this output, DFS will first try to reach the 'Stadium' which is deepest node from the 'University' node. Then it will backtrack and move to another deep node 'Hospital'. Again it will continue to visit all neighboring nodes of this node, skipping over nodes that have already been visited (since they have been visited already).

BFS output: In this output, BFS will first visit the neighboring nodes of 'University'. Then it will visit the neighbors of these neighbors and so on, moving to the next level only after it has visited all nodes at the same distance (i.e., nodes that are reached in the same number of steps from the starting node).

These kinds of outputs usually give us insights into understanding the connections in the network and how specific nodes are linked to each other.
"""
