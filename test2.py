import networkx as nx
import matplotlib.pyplot as plt
import sys
from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from polygons import create_circular_polygon
from det1 import dinvandconquer

pos={}
polygon=create_circular_polygon(20,4)
g = dinvandconquer(polygon)
graph= nx.Graph()

for node in g:
   print(node.x,",",node.y)
   graph.add_node((node.x, node.y))
   pos[(node.x, node.y)] = [float(node.x), float(node.y)]
   
print("edges:")
for node in g:
    for edge in node.edges:
        print(node.x,",", node.y, "<<node")
        print(edge.x,",",edge.y, "<<edge")
        graph.add_edge((node.x, node.y), (edge.x, edge.y))
        
nx.draw_networkx(graph, pos, with_labels = False)
plt.show()


