from operator import itemgetter
import networkx as nx
import random as rand
import math




        
        
class GraphNode:
    def __init__ (self,x,y):
        self.x= x    
        self.y= y 

        self.edges=[]
    
def dinvandconquer (points):

     return divid(sorted(points, key=itemgetter(0)))
    
def merge(left,right):

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

    
