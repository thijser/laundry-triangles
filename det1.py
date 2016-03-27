from operator import itemgetter
import networkx as nx
import random as rand
import math
import triangulation as tr
from math import atan2, degrees, pi



        
        
class GraphNode:
    def __init__ (self,x,y):
        self.x= x    
        self.y= y 
        self.edges=[]
    def __repr__(self):
        st= '{0:.{1}f}'.format((self.x),2),",",'{0:.{1}f}'.format((self.y),2), ",<"
#        for e in self.edges:
#           st+= "(",'{0:.{1}f}'.format((e.x),2),",",'{0:.{1}f}'.format((e.y),2),")"
#        st+=">",
        return ''.join((st))

def dinvandconquer (points):

     return divid(sorted(points, key=itemgetter(0)))

def ValidAngle(a,b,c):
    return 0<((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x))


def angle(a,b,c):

    xa=a.x-c.x
    ya=a.y-c.y
    xb=b.x-c.x
    yb=b.y-c.y 
    la=(xa-xb)*(xa-xb)+(ya-yb)
    lb=(xb*xb)+(yb*yb)
    lc=(xa*xa)+(ya*ya)

    if(2*la*lb<0.00000001):
        return -1
    print((la+lb -lc)/(2*la*lb))
   # try:
    gamma=math.acos((la+lb -lc)/(2*la*lb))
    #catch:
    #  return 180
    # 
    return -gamma%180

def getCandidate(l,i,a,b):
    c=0

    while(i<len(l)):
        global ri
        ri=i
        c=l[i]
        if ((c == a) or (c == b)):
            i=i+1
            continue
        circle=tr.circumcircle([[a.x,a.y],[b.x,b.y],[c.x,c.y]])
        if(i+1<len(l) and (tr.in_circle(circle,[l[i+1].x,l[i+1].y]))):
            i=i+1
            while(i+1<len(l) and ValidAngle(a,b,c)):
                 i=i+1
            continue
        else:
            ri=i+1
            return c;
    return None
    
def merge(left,right):
    left[len(left)-1].edges.add(right[len(right)-1])
    left[0].edges.add(right[0])
    right[0].edges.add(left[0])
    a=left[len(left)-1]
    b=right[len(right)-1]
    ret = []
    ret.append(left.pop())
    ret.append(right.pop())
    i=0
    j=0


    while(1==1):
        left=sorted(left,key = lambda z,x=a,y=b: angle(x,y,z))
        right=sorted(right,key = lambda z,x=b,y=a: angle(x,y,z))
        c = None
        if(len(left)>i):
             cl=getCandidate(left,i,a,b)
        if(cl is not None):
           lcl=cl
        ti=ri
        if(len(right)>j):
            cr=getCandidate(right,j,b,a)
        else:
            cr= None
        if(cr is not None):
           lcr=cr
        else:
            cl= None
        tj=ri
        if((cl is not None) and (cr is not None)):
            circlleft=tr.circumcircle([[a.x,a.y],[b.x,b.y],[cl.x,cl.y]])
            if(tr.in_circle(circlleft,[cr.x,cr.y])):
                cl=None
        if cr is not None:
            c=cr
            j=1
            right.remove(c)
            ret.append(c)
            cl = None
        if(cl is not None):
            c=cl
            i=1
            left.remove(c)
            ret.append(c)
        if(c is None):
            return ret+left+right
        
        c.edges.add(a)
        c.edges.add(b)
        a.edges.add(c)
        b.edges.add(c)
        if(cl is not None):
            b=c
        else:
            a=c
    while(len(left)!=0):
       ret.append(left[0])
       lcl=left[0]
       c.edges.add(left.pop())
    while(len(right)!=0):
       lcr=right[0]
       ret.append(right[0])
       c.edges.add(right.pop())
    lcr.edges.add(lcl)
    lcl.edges.add(lcr)
    return ret

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
        cr=right[i]
        i=i+1
    while(j<len(left)):
        res.append(left[j])
        cr=left[i]
        j=j+1

    return res            
        

def divid(sortedPoints):
    
    if(len(sortedPoints)<3):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        a.edges={b} 
        b.edges={a}
        if(a.y>b.y):
            return [b,a]
        return[a,b]
    if(len(sortedPoints)<4):
        a = GraphNode(sortedPoints[0][0],sortedPoints[0][1])
        b = GraphNode(sortedPoints[1][0],sortedPoints[1][1])
        c= GraphNode(sortedPoints[2][0],sortedPoints[2][1])
        a.edges={b,c}
        b.edges={a,c}
        c.edges={a,b}
        if(a.y>b.y):
           a,b=b,a 
        if(a.y>c.y):
           a,c=c,a
        if(b.y>c.y):
           b,c=c,b
        return [a,b,c]
    left = sortedPoints[:int(len(sortedPoints)/2)]
    right = sortedPoints[int(len(sortedPoints)/2):]
 
    return merge(divid(left),divid(right))

    
