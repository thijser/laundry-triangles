import networkx as nx
import matplotlib.pyplot as plt
import sys
from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from triangulation import draw
from polygons import create_circular_polygon
from det1 import dinvandconquer
from polygons import create_ellipsular_polygon

pos={}
polygon=create_ellipsular_polygon(15,15,6)
g = dinvandconquer(polygon)
graph= nx.Graph()

for node in g:
   graph.add_node((node.x, node.y))
   pos[(node.x, node.y)] = [float(node.x), float(node.y)]
   
for node in g:
    for edge in node.edges:
        graph.add_edge((node.x, node.y), (edge.x, edge.y))
        
nx.draw_networkx(graph, pos, with_labels = False)
plt.show()

draw(chew_triangulation(polygon))

