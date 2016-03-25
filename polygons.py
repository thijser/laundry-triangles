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
    