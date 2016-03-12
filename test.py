import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle

triangle = [[3,0], [3,3], [0,0]]

triangles = chew_triangulation([tuple([0,0]), tuple([2,2]), tuple([2,4]), tuple([1,100]), tuple([0,4])])

graph = nx.Graph()

for triangle in triangles:
    add_triangle(graph, triangle)

nx.draw(graph)

plt.show()
