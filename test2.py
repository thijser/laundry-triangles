import networkx as nx
import matplotlib.pyplot as plt
import sys
from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from polygons import create_circular_polygon
from det1 import dinvandconquer

pos={}
polygon=create_circular_polygon(20,10)
g = dinvandconquer(polygon)
graph= nx.Graph()
for nod in g.nodes:
   graph.add_node(nod.x+","+nod.y)
   pos[nod.x+","+nod.y]=[nod.x,nod.y]
for node in g.nodes:
    for edge in node.edges:
        graph.add_edge((nod.x+","+nod.y),(edge.x+","+edge.y))
nx.draw(graph,pos)


