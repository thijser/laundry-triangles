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
n = 51
repetitions = 10


sys.setrecursionlimit((n+5) * multiplier)

while True:
    poly = create_worst_case(20,50)
    
    temp_timesW = []
    temp_timesA = []   
    
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
        
    difference = sum(temp_timesW) - sum(temp_timesA)
    print(difference)
    draw(chew_triangulation(poly))
    #if difference >= 0.01:
        #draw(chew_triangulation(poly))
        #quit()

#draw(chew_triangulation(create_ellipsular_polygon(20,23,60)))

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
        
        pol = create_worst_case(20, size)
        start_time = time.clock()
        chew_triangulation(pol)
        end_time = time.clock()
        temp_timesA.append(end_time - start_time)
    
    timesW.append(sum(temp_timesW) / (float(repetitions)))
    timesA.append(sum(temp_timesA) / (float(repetitions)))
    sizes.append(size)
    print(timesA[i-1])

plt.plot(sizes,timesW, 'r')
plt.plot(sizes,timesA, 'b')
plt.show()
