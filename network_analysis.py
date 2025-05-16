import networkx as nx
import pandas as pd

df = pd.read_csv("web_traffic_data.csv")
G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(row['source'], row['target'])

nx.write_graphml(G, "traffic_network.graphml")

in_deg = nx.in_degree_centrality(G)
pagerank = nx.pagerank(G)
between = nx.betweenness_centrality(G)

top_pages = pd.DataFrame({
    "Page": list(in_deg.keys()),
    "In-Degree Centrality": list(in_deg.values()),
    "PageRank": list(pagerank.values()),
    "Betweenness Centrality": list(between.values())
})

top_pages.to_csv("top_pages.csv", index=False)
