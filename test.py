import networkx as nx
import matplotlib.pyplot as plt
import sys

from triangulation import chew_triangulation
from triangulation import draw
from triangulation import deterministic_triangulation

from polygons import create_circular_polygon
from polygons import create_random_structure
from polygons import create_ellipsular_polygon
from polygons import create_worst_case

import time


sizes = []
timesW = []
timesA = []
multiplier = 20
n = 21
repetitions = 10


sys.setrecursionlimit((n+5) * multiplier)

#draw(chew_triangulation(create_ellipsular_polygon(20,23,60)))

difference = []
sys.setrecursionlimit((800+5) * multiplier)
for i in range(1,n):
    poly = create_worst_case(20, 800)
    temp_timesW = []
    temp_timesA = []
    
    for j in range(1, repetitions):
        pol = list(poly)
        start_time = time.clock()
        deterministic_triangulation(pol)
        end_time = time.clock()
        temp_timesW.append(end_time - start_time)
        
        pol = list(poly)
        start_time = time.clock()
        chew_triangulation(pol)
        end_time = time.clock()
        temp_timesA.append(end_time - start_time)

    timesW.append(sum(temp_timesA) / (float(repetitions)))
    timesA.append(sum(temp_timesA) / (float(repetitions)))
    difference.append(timesW[i-1] - timesA[i-1])
    sizes.append(i)
    
#plt.plot(sizes,timesW, 'r')
#plt.plot(sizes,timesA, 'b')
plt.plot(sizes,difference)
plt.show()
    
quit()

for i in range(1,n):
    size = i*multiplier
    
    temp_timesW = []
    temp_timesA = []
    
    for j in range(0,repetitions):
        pol = create_worst_case(20, size)
        start_time = time.clock()
        deterministic_triangulation(pol)
        end_time = time.clock()
        temp_timesW.append(end_time - start_time)
        
        pol = create_circular_polygon(20, size)
        start_time = time.clock()
        deterministic_triangulation(pol)
        end_time = time.clock()
        temp_timesA.append(end_time - start_time)
    
    timesW.append(sum(temp_timesW) / (float(repetitions)))
    timesA.append(sum(temp_timesA) / (float(repetitions)))
    sizes.append(size)
    print(timesA[i-1])

plt.plot(sizes,timesW, 'r')
plt.plot(sizes,timesA, 'b')
plt.show()
