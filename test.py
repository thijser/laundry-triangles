import networkx as nx
import matplotlib.pyplot as plt
import sys

from triangulation import chew_triangulation
from triangulation import draw
from triangulation import deterministic_triangulation

from det1 import dinvandconquer

from polygons import create_circular_polygon
from polygons import create_random_structure
from polygons import create_ellipsular_polygon
from polygons import create_worst_cases
from polygons import create_almost_worst_cases

import time


sizes = []
timesC = []
timesDC = []
timesD = []
multiplier = 200
n = 51
repetitions = 10

max_n = 60

sys.setrecursionlimit((n+10) * multiplier)

cases = []
while len(cases) < max_n-3:
    cases = create_worst_cases(40, 80, max_n, 1.0/2000.0, 300)

for i in range(0,len(cases)):
    size = i * multiplier
    temp_timesC = []
    temp_timesDC = []
    temp_timesD = []
    
    poly = cases[i]
    
    for j in range(0,repetitions):        
        pol = list(poly)
        start_time = time.perf_counter()
        chew_triangulation(pol)
        end_time = time.perf_counter()
        temp_timesC.append(end_time - start_time)
        
        pol = list(poly)
        start_time = time.perf_counter()
        deterministic_triangulation(pol)
        end_time = time.perf_counter()
        temp_timesDC.append(end_time - start_time)
        
        pol = list(poly)
        start_time = time.perf_counter()
        #dinvandconquer(pol)
        end_time = time.perf_counter()
        temp_timesD.append(end_time - start_time)
        
    sizes.append(i+3)
    timesC.append(sum(temp_timesC) / float(repetitions))
    timesDC.append(sum(temp_timesDC) / float(repetitions))
    timesD.append(sum(temp_timesD) / float(repetitions))
    print(timesC[i-1])
    
plt.plot(sizes,timesC, 'b', label = "Chew's algorithm")
plt.plot(sizes, timesDC, 'r', label = "Derandomized Chew's algorithm")
plt.plot(sizes, timesD, 'k', label = "Divide and conquer")

plt.xlabel("Number of points")
plt.ylabel("Runtime (in seconds)")

plt.legend(loc=2)

plt.show()
