import networkx as nx
import matplotlib.pyplot as plt
import sys
import math

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
multiplier = 20
n = 51
repetitions = 10

max_n = 80

sys.setrecursionlimit((n+10) * multiplier)

for i in range(1,n):
    size = (n-i) * multiplier
    temp_timesC = []
    temp_timesDC = []
    temp_timesD = []
    
    for j in range(0,repetitions):
        poly = create_ellipsular_polygon(20,30,size)
        
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
        dinvandconquer(pol)
        end_time = time.perf_counter()
        temp_timesD.append(end_time - start_time)
        
    sizes.append(size)
    timesC.append(sum(temp_timesC) / float(repetitions))
    timesDC.append((sum(temp_timesDC) / float(repetitions)))
    timesD.append(sum(temp_timesD) / float(repetitions))
    print(i,"dd")
    print(timesC[i-1])
    print(timesDC[i-1])
    print(timesD[i-1])
    
plt.plot(sizes,timesC, 'b', label = "Chew's algorithm")
plt.plot(sizes, timesDC, 'r', label = "Derandomized Chew's algorithm")
plt.plot(sizes, timesD, 'k', label = "Divide and conquer")

plt.xlabel("Number of points")
plt.ylabel("Runtime (in seconds)")

plt.legend(loc=2)

plt.show()
print()
print()
print(timesC)
print()
print()
print(timesDC)
print()
print()
print(timesD)
print()
print()
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
    print(i,"wc")
    

plt.plot(sizes,timesW, 'r')
plt.plot(sizes,timesA, 'b')
plt.show()

