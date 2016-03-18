import networkx as nx
import random as rand
import math

def nodeString(point):
    return str(point[0]) + "," + str(point[1])

def add_triangle(graph, pos, points):
    for i in range(0,3):
        graph.add_node(nodeString(points[i]))
        pos[nodeString(points[i])] = points[i]  

    for i in range(0,3):
        for j in range(i+1,3):
            graph.add_edge(nodeString(points[i]),nodeString(points[j]))

def dot_product(x,y):
    ret = x[0]*y[0] + x[1]*y[1]
    return ret

def perpendicular(a,b):
    origin = [(a[0] + b[0])/2.0, (a[1] + b[1])/2.0]
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

    origin =  [con * h2[1][0] + h2[0][0], con * h2[1][0] + h2[0][0]]

    radius = dist(origin, c)

    return [origin, radius]

def dist(a,b):
    x = math.pow(a[0] - b[0], 2)
    y = math.pow(a[1] - b[1], 2)
    return math.sqrt(x + y)

def in_circle(circle, point):
    return dist(circle[0], point) <= circle[1]

def all_perm(triangle):
    return [tuple([a,b,c]) for a in triangle for b in triangle for c in triangle if a != b and a != c and b != c]

def chew_triangulation(points):
    if len(points) < 3:
        raise ValueError("Not enough points")    

    if len(points) == 3:
        return [tuple(points)]
         
    p_i = rand.randint(0,len(points)-1)
    q_i = (p_i - 1) % len(points);
    r_i = (p_i + 1) % len(points);

    p = points[p_i]
    q = points[q_i]
    r = points[r_i]

    de = chew_triangulation(points[0:p_i] + points[p_i+1:])
        
    S = [triangle for triangle in de if in_circle(circumcircle(triangle), p)]
    S.append(tuple([p,q,r]))

    toRemove = set([])
    toAdd = []

    edges = {}
    for triangle in S: 
        for i in range(0,3):
            for j in range(i+1,3):
                edgeA = (triangle[i], triangle[j])
                edgeB = (triangle[j], triangle[i])

                if edgeA in edges:
                    triangle_b = edges[edgeA]
                
                    toRemove.update(all_perm(triangle))
                    toRemove.update(all_perm(triangle_b))
                    
                    add = [tuple([triangle[a],triangle[b],p]) for a in range(0,3) for b in range(a+1,3) if triangle[a] != p and triangle[b] != p]
                    toAdd.extend(add)
                    add = [tuple([triangle_b[a],triangle_b[b],p]) for a in range(0,3) for b in range(a+1,3) if triangle_b[a] != p and triangle_b[b] != p]
                    toAdd.extend(add)
                
                else:
                    edges[edgeA] = triangle
                    edges[edgeB] = triangle
      
    de.append((p,q,r))
    de.extend(toAdd)

    return [triangle for triangle in de if triangle not in toRemove]

