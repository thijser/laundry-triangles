from operator import itemgetter
import networkx as nx
import random as rand
import math


class Graph
	def__init__(self,nodes)
		self.nodes=nodes
		self.lowest = min(i.x for i in nodes)
		
		
class GraphNode
	def__init__ (self,x,y)
		self.x= x	
		self.y= y 

		self.edges=[]
	
def dinvandconquer (points)
	sorted(points, key=itemgetter(0))

	
def merge(left,right)
	
	
	
	
	
	
	
	
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
	
	if(len(sortedPoints<3)):
		a = GraphNode(sortedpoints[0][0],sortedpoints[0][1])
		b = GraphNode(sortedpoints[1][0],sortedpoints[1][1])
		a.edges[0]=b 
		b.edges[0]=a
		return Graph([a,b])
		
	if(len(sortedPoints<4)):
		a = GraphNode(sortedpoints[0][0],sortedpoints[0][1])
		b = GraphNode(sortedpoints[1][0],sortedpoints[1][1])
		c= GraphNode(sortedpoints[2][0],sortedpoints[2][1])
				
		a.edges[0]=b 
		a.edges[1]=c
		b.edges[0]=a
		b.edges[1]=c
		c.edges[0]=a
		c.edges[0]=b 
		return Graph([a,b,c])
		

	left = sortedPoints[:len(A)/2]
	right = sortedPoints[len(A)/2:]
	return merge(divid(left),divid(right))

	
