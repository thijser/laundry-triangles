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
<<<<<<< HEAD
n = 300
=======
n = 20
repetitions = 10
>>>>>>> 1bf9ac19a8e8bb1fbeaf162086107ead0cc2f179

sys.setrecursionlimit((n+5) * multiplier)

for i in range(1,n):
    size = i*multiplier
<<<<<<< HEAD
    pol = create_circular_polygon(20,size) #For testing multiple algs we should first copy this
    start_time = time.clock()
    draw(chew_triangulation(pol))
    end_time = time.clock()    
    times.append(end_time - start_time)
=======
    
    temp_times = []
    
    for j in range(0,repetitions):
        pol = create_circular_polygon(20,size)
        start_time = time.clock()
        chew_triangulation(pol)
        end_time = time.clock()
        temp_times.append(end_time - start_time)
    
    times.append(sum(temp_times) / (float(repetitions)))
>>>>>>> 1bf9ac19a8e8bb1fbeaf162086107ead0cc2f179
    sizes.append(size)
    print(times[i-1])

plt.plot(sizes,times)
plt.show()    

draw(chew_triangulation(create_circular_polygon(20,35)))
