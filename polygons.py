import random as rand
import math

from decimal import *

from triangulation import chew_triangulation
from triangulation import find_S
from triangulation import update_graph
from triangulation import add_triangle

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
    
def create_worst_cases(radius, num_points, epsilon, start_area):
    func = lambda p : (Decimal(radius*math.cos(p*2*math.pi)), Decimal(radius*math.sin(p*2*math.pi)))
    
    cases = []
    
    ps = create_polygon(lambda p : p/float(start_area), 3)
    points = [func(p) for p in ps]
    
    graph = chew_triangulation(list(points))
    
    cases.append(list(points))
    
    for i in range(0, num_points - 3):
        p = ps[len(ps)-1] + epsilon
        
        if p >= 1:
            print("Only got to " + str(len(points)) + " points :-(")
            return cases
        
        q = points[len(points)-1]
        r = points[0]
                        
        maxp = p
        max = 0
        
        while p < 1:
            S = find_S(graph, func(p), q, r)
            if len(S) > max:
                max = len(S)
                maxp = p
            p += epsilon
            
        ps.append(maxp)
        point = func(maxp)
        points.append(point)
        
        S = find_S(graph, point, q, r)
        add_triangle(graph, (point,q,r))
        
        update_graph(graph, S, point)
        
        cases.append(list(points))
        
    return cases
    
   
def create_almost_worst_cases(radius, num_points, epsilon):
    func = lambda p : (Decimal(radius*math.cos(p*2*math.pi)), Decimal(radius*math.sin(p*2*math.pi)))
    
    cases = []
    
    area = 1.0/num_points
    
    ps = create_polygon(lambda p : p*area, 3)
    points = [func(p) for p in ps]
    
    graph = chew_triangulation(list(points))
    
    cases.append(list(points))
    
    for i in range(0, num_points - 3):
        p = ps[len(ps)-1] + epsilon
        
        if p >= 1:
            print("Only got to " + str(len(points)) + " points :-(")
            return cases
        
        q = points[len(points)-1]
        r = points[0]
                        
        maxp = p
        max = 0
        
        while p < 1 and p < (i+4)*area:
            S = find_S(graph, func(p), q, r)
            if len(S) > max:
                max = len(S)
                maxp = p
            p += epsilon
            
        ps.append(maxp)
        point = func(maxp)
        points.append(point)
        
        S = find_S(graph, point, q, r)
        add_triangle(graph, (point,q,r))
        
        update_graph(graph, S, point)
        
        cases.append(list(points))
        
    return cases