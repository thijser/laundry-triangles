import networkx as nx
import random as rand
import math
import time
import matplotlib.pyplot as plt

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

def draw(triangles):
    graph = nx.Graph()
    pos = {}
	
    for triangle in triangles:
      add_triangle(graph, pos, triangle)
    nx.draw(graph, pos)
    plt.show()
    time.sleep(0.5)



def find_shared_edges(triangles):
    shared_edges = set()
    sharing_triangles = set()
    
    edges = {}
    for triangle in triangles: 
        for i in range(0,3):
            for j in range(i+1,3):
                edgeA = (triangle[i], triangle[j])
                edgeB = (triangle[j], triangle[i])

                if edgeA in edges:
                    shared_edges.add(edgeA)
                    shared_edges.add(edgeB)
                    sharing_triangles.add(triangle)
                    sharing_triangles.add(edges[edgeA])
                
                else:
                    edges[edgeA] = triangle
                    edges[edgeB] = triangle
                    
    return [shared_edges, sharing_triangles]
    
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
    draw(de)
    S = [triangle for triangle in de if in_circle(circumcircle(triangle), p)]
    S.append(tuple([p,q,r]))

    triangles_to_remove = set()
    triangles_to_add = []

    shared = find_shared_edges(S)
    
    edges_to_remove = shared[0]
    triangles_to_remove = shared[1]
    
    edges = set()
    edges.update([(triangle[a],triangle[b]) for triangle in triangles_to_remove for a in range(0,3) for b in range(a+1,3)])
    triangles_to_add = [(a,b,p) for (a,b) in edges if a != p and b != p and (a, b) not in edges_to_remove]
      
    de.append((p,q,r))
    de = [triangle for triangle in de if triangle not in triangles_to_remove]
    de.extend(triangles_to_add)

    return de

