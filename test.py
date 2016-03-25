import networkx as nx
import matplotlib.pyplot as plt
import sys

from triangulation2 import chew_triangulation
from triangulation2 import draw

from polygons import create_circular_polygon

import time


sizes = []
times = []
multiplier = 20
n = 300

sys.setrecursionlimit((n+5) * multiplier)

for i in range(1,n):
    size = i*multiplier
    pol = create_circular_polygon(20,size) #For testing multiple algs we should first copy this
    start_time = time.clock()
    draw(chew_triangulation(pol))
    end_time = time.clock()    
    times.append(end_time - start_time)
    sizes.append(size)
    print(times[i-1])

plt.plot(sizes,times)
plt.show()    

draw(chew_triangulation(create_circular_polygon(20,5)))
triangles = chew_triangulation([(-4,-2),(-3,-2),(2,2),(5,2),(-2,-3)])

triangle = ((0.0,0.0), (0.1,0.1), (0.0,15.0))
print(circumcircle(triangle))

draw(triangles)

