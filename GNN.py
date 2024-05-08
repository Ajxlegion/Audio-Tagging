import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Nodes
nodes = [0, 1, 1, 0, 0, 1, 1, 1]

# Edges
edges = [2, 1, 1, 1, 2, 1, 1]

# Adjacency List
adjacency_list = [[1, 0], [2, 0], [4, 3], [6, 2], [7, 3], [7, 4], [7, 5]]

# Global Attribute
global_attribute = 0

# Add nodes to the graph
for node_id, node_value in enumerate(nodes):
    G.add_node(node_id, value=node_value)

# Add edges to the graph
for i, edge_weight in enumerate(edges):
    G.add_edge(i, i+1, weight=edge_weight)

# Set global attribute
G.graph['global'] = global_attribute

# Visualize the graph
pos = nx.spring_layout(G, seed=42)
labels = nx.get_node_attributes(G, 'value')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("Sample Graph")
plt.show()
