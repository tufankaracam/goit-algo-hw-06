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


def dfs_paths(graph, start):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        # print("DFS at node: ", vertex)
        for next in graph[vertex] - set(path):
            stack.append((next, path + [next]))
    return path


def bfs_paths(graph, start):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        # print("BFS at node: ", vertex)
        for next in graph[vertex] - set(path):
            queue.append((next, path + [next]))
    return path


graph = {vertex: set([t for t in G.neighbors(vertex)]) for vertex in G}

print("\nDFS path: ", dfs_paths(graph, 'University'))
print("\nBFS path: ", bfs_paths(graph, 'University'))

"""
Depth-First Search (DFS) and Breadth-First Search (BFS) are algorithms that traverse or search a graph or network and determine how one can reach other nodes from a particular starting node.

DFS prefers to go deeper into the graph by exploring from the first node it discovers, then it backtracks, whereas BFS aims to visit all nodes at the same level (i.e., equally distant from the starting node) first.

We can see these properties from their outputs.

DFS output: In this output, DFS will first try to reach the 'Stadium' which is deepest node from the 'University' node. Then it will backtrack and move to another deep node 'Hospital'. Again it will continue to visit all neighboring nodes of this node, skipping over nodes that have already been visited (since they have been visited already).

BFS output: In this output, BFS will first visit the neighboring nodes of 'University'. Then it will visit the neighbors of these neighbors and so on, moving to the next level only after it has visited all nodes at the same distance (i.e., nodes that are reached in the same number of steps from the starting node).

These kinds of outputs usually give us insights into understanding the connections in the network and how specific nodes are linked to each other.
"""
