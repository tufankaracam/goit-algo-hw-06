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
