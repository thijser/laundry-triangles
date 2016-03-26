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
timesW = []
timesA = []
multiplier = 20
n = 21
repetitions = 50

max_n = 80

sys.setrecursionlimit((max_n+10) * multiplier)

cases = []
while len(cases) < max_n - 20:
    cases = create_worst_cases(80, max_n, 1.0/6000.0, 300)

for i in range(0,len(cases)):    
    temp_timesW = []
    temp_timesA = []
    
    poly = cases[i]
    
    for j in range(0,repetitions):
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
    
    timesW.append(sum(temp_timesW) / (float(repetitions)))
    timesA.append(sum(temp_timesA) / (float(repetitions)))
    sizes.append(len(poly))
    print(timesA[i-1])

plt.plot(sizes,timesW, 'r')
plt.plot(sizes,timesA, 'b')
plt.show()
