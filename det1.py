from operator import itemgetter
import networkx as nx
import random as rand
import math


class Graph:
    def __init__(self,nodes):
        self.nodes=nodes

        
        
class GraphNode:
    def __init__ (self,x,y):
        self.x= x    
        self.y= y 

        self.edges=[]
    
def dinvandconquer (points):
     return divid(sorted(points, key=itemgetter(0)))
    
def merge(left,right):
    left.nodes[0].edges.append(right.nodes[0]);

    return Graph(mergelist(left.nodes,right.nodes));
     
    
    
def mergeLists(left,right):
    if(left[len(left)-1])>right[len(right)-1]:
        left,right = right,left
    res=[]
    j=0;
    i=0;
    
    while(i<len(right)):
        if(left[i][1]<right[j][1]):
            res[i+j]=left[i]
            i=i+1;
        else:
            res[i+j]=right[j]
            j=j+1;        
                
        

def divid(sortedPoints):
    
    if(len(sortedPoints)<3):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        a.edges[0]=b 
        b.edges[0]=a
        return Graph([a,b])
        
    if(len(sortedPoints)<4):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        c= GraphNode(sortedPoints[2][0],sortedPoints[2][1])
                
        a.edges[0]=b 
        a.edges[1]=c
        b.edges[0]=a
        b.edges[1]=c
        c.edges[0]=a
        c.edges[0]=b 
        return Graph([a,b,c])
        

    left = sortedPoints[:int(len(sortedPoints)/2)]
    right = sortedPoints[int(len(sortedPoints)/2):]
    return merge(divid(left),divid(right))

    
