import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from triangulation import chew_triangulation

graph = chew_triangulation([[1,1], [2,2], [3,3]])

nx.draw(graph)

plt.show()
