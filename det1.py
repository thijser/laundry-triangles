from operator import itemgetter
import networkx as nx
import random as rand
import math
import triangulation as tr




        
        
class GraphNode:
    def __init__ (self,x,y):
        self.x= x    
        self.y= y 
        self.edges=[]
    
def dinvandconquer (points):

     return divid(sorted(points, key=itemgetter(0)))
    
def merge(left,right):
    left[0].edges.add(right[0])
    i=0
    j=0
    a=left[0]
    b=right[0]
    c=left[0]

    while((i<len(left)-1)&(j<len(right)-1)):
        circle=tr.circumcircle([[a.x,a.y],[b.x,b.y],[left[i+1].x,left[i+1].x]])
        if (tr.in_circle(circle,[right[i+j].x,right[i+1].y])):
            c=left[j+1]
            c.edges.add(b)
            c.edges.add(a)
            b.edges.add(c)
            a.edges.add(c)
            a=c
            j=j+1
        else:
            c=right[i+1]
            c.edges.add(b)
            c.edges.add(a)
            b.edges.add(c)
            a.edges.add(c)
            a=c
            i=i+1
            
    left[len(left)-1].edges.add(right[len(right)-1])
    right[len(right)-1].edges.add(left[len(left)-1])
    return mergeLists(left,right)
   
    
def mergeLists(left,right):
    if(left is None):
        return right
    if right is None:
        return left
    res=[]
    j=0;
    i=0;
    while(i<len(right)&j<len(left)):
     
        if(left[i].y<right[j].y):
            res.append(left[i])
            i=i+1;
        else:
            res.append(right[j])
            j=j+1;        

    while(i<len(right)):
        res.append(right[i])
        i=i+1
    while(j<len(left)):
        res.append(left[j])
        j=j+1

    return res            
        

def divid(sortedPoints):
    
    if(len(sortedPoints)<3):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        a.edges={b} 
        b.edges={a}
        return [a,b]
        
    if(len(sortedPoints)<4):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        c= GraphNode(sortedPoints[2][0],sortedPoints[2][1])
                
        a.edges={b,c}
        b.edges={a,c}
        c.edges={a,b}
        return [a,b,c]
        

    left = sortedPoints[:int(len(sortedPoints)/2)]
    right = sortedPoints[int(len(sortedPoints)/2):]
 
    return merge(divid(left),divid(right))

    
