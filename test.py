import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle

from polygons import create_circular_polygon

triangle = [[3,0], [3,3], [0,0]]

#triangles = chew_triangulation(create_circular_polygon(70,20))
triangles = chew_triangulation([(-4,-2),(-3,-2),(2,2),(5,2),(-2,-2)])
graph = nx.Graph()
pos = {}

for triangle in triangles:
    add_triangle(graph, pos, triangle)

nx.draw(graph, pos)

plt.show()
