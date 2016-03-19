import networkx as nx
import matplotlib.pyplot as plt

from triangulation import chew_triangulation
from triangulation import circumcircle
from triangulation import add_triangle
from triangulation import draw

from polygons import create_circular_polygon

triangles = chew_triangulation(create_circular_polygon(35,10))
#triangles = chew_triangulation([(-4,-2),(-3,-2),(2,2),(5,2),(-2,-3)])

#triangle = ((0.0,0.0), (0.1,0.1), (0.0,15.0))
#print(circumcircle(triangle))

draw(triangles)
