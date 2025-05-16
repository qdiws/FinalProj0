import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_graphml("traffic_network.graphml")
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=20, alpha=0.7, edge_color="gray", with_labels=False)
plt.title("Website Traffic Flow Network")
plt.show()
