import random as rand
import math

def create_circular_polygon(radius, num_points):
    func = lambda p : (math.cos(p*2*math.pi)*radius, math.sin(p*2*math.pi)*radius)
       
    return create_polygon(func, num_points)
    
def create_polygon(func, num_points):    
    points = [rand.random() for i in range(0,num_points)]
    points.sort()
    
    return [func(p) for p in points]