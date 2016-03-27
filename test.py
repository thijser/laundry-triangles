import networkx as nx
import matplotlib.pyplot as plt
import sys

from triangulation import chew_triangulation
from triangulation import draw
from triangulation import deterministic_triangulation

from polygons import create_circular_polygon
from polygons import create_random_structure
from polygons import create_ellipsular_polygon
from polygons import create_worst_cases
from polygons import create_almost_worst_cases

import time


sizes = []
times = []
timesW = []
timesA = []
multiplier = 50
n = 201
repetitions = 20

max_n = 80

sys.setrecursionlimit((n+10) * multiplier)

for i in range(1,n):
    size = i * multiplier
    temp_times = []
    
    for j in range(0,repetitions):
        pol = create_ellipsular_polygon(20,30,size)
        start_time = time.perf_counter()
        chew_triangulation(pol)
        end_time = time.perf_counter()
        temp_times.append(end_time - start_time)
        
    sizes.append(size)
    times.append(sum(temp_times) / float(repetitions))
    print(times[i-1])
    
plt.plot(sizes,times, 'b')
plt.xlabel("Number of points")
plt.ylabel("Runtime (in seconds)")

plt.show()

quit()

cases = []
while len(cases) < max_n - 20:
    cases = create_worst_cases(80, max_n, 1.0/6000.0, 300)

for i in range(0,len(cases)):    
    temp_timesW = []
    temp_timesA = []
    
    poly = cases[i]
    
    for j in range(0,repetitions):
        pol = list(poly)
        start_time = time.perf_counter()
        deterministic_triangulation(pol)
        end_time = time.perf_counter()
        temp_timesW.append(end_time - start_time)
        
        pol = list(poly)
        start_time = time.perf_counter()
        chew_triangulation(pol)
        end_time = time.perf_counter()
        temp_timesA.append(end_time - start_time)
    
    timesW.append(sum(temp_timesW) / (float(repetitions)))
    timesA.append(sum(temp_timesA) / (float(repetitions)))
    sizes.append(len(poly))
    print(timesA[i-1])

plt.plot(sizes,timesW, 'r')
plt.plot(sizes,timesA, 'b')
plt.show()
