# Task 1
import networkx as nx
import matplotlib.pyplot as plt

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

pos = nx.spring_layout(G)

print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

for node in G.nodes():
    print("Degree of", node, ":", G.degree(node))

nx.draw(G, pos=pos, with_labels=True)
plt.show()
