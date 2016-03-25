import networkx as nx
import random as rand
import math
import matplotlib.pyplot as plt

from decimal import *

def add_triangle(graph, points):
    for i in range(0,3):
        graph.add_node(points[i])

    for i in range(0,3):
        for j in range(i+1,3):
            graph.add_edge(points[i],points[j])

def dot_product(x,y):
    ret = x[0]*y[0] + x[1]*y[1]
    return ret

def perpendicular(a,b):
    origin = [(a[0] + b[0])/Decimal('2'), (a[1] + b[1])/Decimal('2')]
    vec = [a[1] - b[1], b[0] - a[0]]
    return [origin, vec]

def circumcircle(triangle):
    #http://stackoverflow.com/questions/3252194/numpy-and-line-intersections
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]

    h1 = perpendicular(a,b)
    h2 = perpendicular(b,c)

    l = [b[0] - a[0], b[1] - a[1]]

    num = dot_product(l, [h1[0][0] - h2[0][0], h1[0][1] - h2[0][1]])
    denom = dot_product(l, h2[1])

    con = num/denom

    origin =  [con * h2[1][0] + h2[0][0], con * h2[1][1] + h2[0][1]]

    radius = dist(origin, c)

    return [origin, radius]

def dist(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x*x + y*y).sqrt()

def in_circle(circle, point):
    return dist(circle[0], point) <= circle[1]

def draw(graph):
    pos = {}
    
    for node in graph:
        pos[node] = [float(node[0]), float(node[1])]
    
    nx.draw_networkx(graph, pos, with_labels = False)
    plt.show()

def find_S(graph, p, q, r):
    to_check = set()
    to_check.add(q)
    to_check.add(r)
    
    checked = set()
    
    S = []
    
    while to_check:
        point = to_check.pop()
        checked.add(point)
        
        neighbors = [n for n in graph[point] if n not in checked]        
        triangles = [(point, neighbors[n1], neighbors[n2]) for n1 in range(0,len(neighbors)) for n2 in range(n1+1,len(neighbors)) if graph.has_edge(neighbors[n1], neighbors[n2])]        
        invalid = [triangle for triangle in triangles if in_circle(circumcircle(triangle), p)]
        
        S.extend(invalid)
        
        to_check.update([triangle[i] for triangle in invalid for i in range(1,3)])
        
    S.append((p,q,r))
    
    return S

def update_graph(graph, S, p):
    edges = set()
    
    for triangle in S:
        for i in range(0,3):
            for j in range(i+1,3):
                edgeA = (triangle[i], triangle[j])
                
                if edgeA in edges:
                    graph.remove_edge(triangle[i], triangle[j])
                else:
                    edgeB = (triangle[j], triangle[i])
                    edges.add(edgeA)
                    edges.add(edgeB)
                    
    for triangle in S:
        for point in triangle:
            if point != p:
                graph.add_edge(point, p)
    
def chew_triangulation(points):
    if len(points) < 3:
        raise ValueError("Not enough points")    

    if len(points) == 3:
        G = nx.Graph()
        add_triangle(G, points)
        return G
         
    p_i = rand.randint(0,len(points)-1)
    q_i = (p_i - 1) % len(points);
    r_i = (p_i + 1) % len(points);

    p = points[p_i]
    q = points[q_i]
    r = points[r_i]

    points.pop(p_i)
    G = chew_triangulation(points)
    
    S = find_S(G, p, q, r)
    
    add_triangle(G, (p,q,r))
    
    update_graph(G, S, p)
    
    return G
        
    

