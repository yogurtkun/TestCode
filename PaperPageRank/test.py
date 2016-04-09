import networkx as nx
import matplotlib.pyplot as plt

graph = nx.DiGraph()
graph.add_nodes_from(['a','b','c','d'])
graph.add_edges_from([('a','b'),('c','b'),('d','c')],key = 'test')

scores = nx.pagerank(graph)
print(scores)

plt.figure(1)
nx.draw(graph,node_size=[x * 6000 for x in scores],with_labels=True)
plt.show()