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
n = 20
repetitions = 10

sys.setrecursionlimit((n+5) * multiplier)

for i in range(1,n):
    size = i*multiplier
    
    temp_times = []
    
    for j in range(0,repetitions):
        pol = create_circular_polygon(20,size)
        start_time = time.clock()
        chew_triangulation(pol)
        end_time = time.clock()
        temp_times.append(end_time - start_time)
    
    times.append(sum(temp_times) / (float(repetitions)))
    sizes.append(size)
    print(times[i-1])

plt.plot(sizes,times)
plt.show()    

draw(chew_triangulation(create_circular_polygon(20,35)))
