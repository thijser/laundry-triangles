import networkx as nx
import random as rand

def nodeString(point):
    return str(point[0]) + "," + str(point[1])

def add_triangle(graph, points):
    graph.add_node(nodeString(points[0]))
    graph.add_node(nodeString(points[1]))
    graph.add_node(nodeString(points[2]))

    for i in range(0,3):
        for j in range(i+1,3):
            graph.add_edge(nodeString(points[i]),nodeString(points[j]))



def chew_triangulation(points):
    if len(points) < 3:
        raise ValueError("Not enough points")    

    if len(points) == 3:
        triangle = nx.Graph()

        addTriangle(triangle, points)

        return triangle
         
    p_i = rand.randint(0,len(points)-1)
    q_i = (p_i - 1) % len(points);
    r_i = (p_i + 1) % len(points);

    graph = chew_triangulation(points[0:p_i] + points[p_i+1:])
    

    #add_triangle(D, [points[p_i], points[q_i], points[r_i]])

    

    return nx.Graph()

