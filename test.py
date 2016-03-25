import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from det1 import dinvandconquer

from polygons import create_circular_polygon

triangle = [[3,0], [3,3], [0,0]]
chew_triangulation
polygon=create_circular_polygon(70,20)

triangles = chew_triangulation(polygon)
graph = nx.Graph()
pos = {}

for triangle in triangles:
    add_triangle(graph, pos, triangle)

nx.draw(graph, pos)

plt.show()

pos={}
g = dinvandconquer(polygon)
graph= nx.Graph()
for nod in g.nodes
   graph.add_node(nod.x+","+nod.y)
   pos[nod.x+","+nod.y]=[nod.x,nod.y]
for node in g.nodes
    for edge in node.edges
        graph.add_edge((nod.x+","+nod.y),(edge.x+","+edge.y))
nx.draw(graph,pos)
