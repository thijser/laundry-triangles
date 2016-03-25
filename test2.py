import networkx as nx
import matplotlib.pyplot as plt
import sys
from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from polygons import create_circular_polygon
from det1 import dinvandconquer

pos={}
polygon=create_circular_polygon(20,30)
g = dinvandconquer(polygon)
graph= nx.Graph()
for nod in g:
   graph.add_node('{0:f}'.format(nod.x)+","+'{0:f}'.format(nod.y))
   pos['{0:f}'.format(nod.x)+","+'{0:f}'.format(nod.y)]=['{0:f}'.format(nod.x),'{0:f}'.format(nod.y)]
for node in g:
    for edge in node.edges:
        graph.add_edge(('{0:f}'.format(nod.x)+","+'{0:f}'.format(nod.y)),('{0:f}'.format(edge.x)+","+'{0:f}'.format(edge.y)))
nx.draw(graph,pos)


