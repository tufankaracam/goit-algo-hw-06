# Task 3


import networkx as nx

G = nx.Graph()

edges = [
    ("Bus Terminal", "University", 7),
    ("University", "Library", 2),
    ("Library", "Shopping Mall", 3),
    ("Shopping Mall", "Stadium", 4),
    ("Stadium", "Airport", 7),
    ("Airport", "Museum", 1),
    ("Museum", "Bus Terminal", 8),
    ("Shopping Mall", "Hospital", 2),
    ("Hospital", "Cinema", 5),
    ("Cinema", "Bus Terminal", 4),
    ("University", "Cafe", 3),
    ("Cafe", "Airport", 5),
    ("Cinema", "Stadium", 3),
    ("Museum", "University", 6),
    ("Hospital", "Stadium", 4),
]

G.add_weighted_edges_from(edges)


def dijkstra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = [n for n in graph.neighbors(current_node)]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.edges[current_node,
                                 next_node]['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path


print("Dijkstra shortest path: ", dijkstra(G, 'University', 'Hospital'))
