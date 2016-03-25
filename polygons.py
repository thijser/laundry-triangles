import random as rand
import math

from decimal import *

def create_circular_polygon(radius, num_points):
    return create_ellipsular_polygon(radius, radius, num_points)

def create_ellipsular_polygon(a, b, num_points):
    func = lambda p : (Decimal(a*math.cos(p*2*math.pi)), Decimal(b*math.sin(p*2*math.pi)))
    
    return create_polygon(func, num_points)
    
def create_polygon(func, num_points):    
    points = [rand.random() for i in range(0,num_points)]
    points.sort()
    
    return [func(p) for p in points]
    
def create_random_structure(num_points):
    mult = 50;
    return [(Decimal(rand.random()*50), Decimal(rand.random()*50)) for i in range(0,num_points)]
    
def create_worst_case(radius, num_points):
    func = lambda p : (Decimal(radius*math.cos(p*2*math.pi)), Decimal(radius*math.sin(p*2*math.pi)))
    step_size = (1.0/5.0)/(num_points/3.0)
    
    points = set()
    pos = 0.0;
    
    while len(points) < num_points:
        for i in range(1, rand.randint(0,int(num_points/1.5))):
            pos += step_size
            points.add(pos % 1)
        pos += rand.random() / 6.0
        
    points = list(points)
    points.sort()
    
    return [func(p) for p in points]
    