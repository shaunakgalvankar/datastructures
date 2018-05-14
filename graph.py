#this is the python implementation of the graph ADT
#here i added two classes (graph,vertex)
#the graph class holds the values of the vertices in form of a dictionary and has methods that operate o it
#the vertex class is also a dictionary structure to hold the edges and the weights info about hte graph


class Vertex:


	def __init__ (self,key):				#the constructor defines the connections as a dictionary 
		self.id=key							#of key value pairs where the keys are the vertices
		self.connectedto={}					#the graph is connected to and the values are the weights 
											#associated with it.
	def addnbr(self,nbr,weight=0):
		self.connectedto[nbr]=weight
#this method adds a neighbour(vertex) as the key and the weight which is initialised to zero is 
#added as the value

	
	def __str__(self):
		        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


	def getconn(self):
		return self.connectedto.keys()
#gets all the vertices connected to a given vertex which is recognised by an id

	def getweight(self):
		return self.connectedto[nbr]
#does pretty much what it says it does

	def getid(self):
		return self.id
#come on i dont need a comment for this one

class Graph:
	
	#constructor which initializes an empty dictionary and the number of vertices to zero
	def __init__(self):
		self.vertices={}
		self.numvert=0

	#adds a vertex to the graph
	def addvertex(self,key):
		self.numvert=self.numvert+1		#increases the number of vertices by one
		newvertex=Vertex(key)			#make an object of the vertex class and assign it to a variable
		self.vertices[key]=newvertex	#append it to the dictionary with the key(name of the vert) and the value to be the actual object
		return newvertex				#return the object that was added to the graphs dictionary	

	def getvertex(self,n):
		if n in self.vertices:
			return self.vertices[n]
		else:
			return "not a vertex"


	def addedge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)				#if the from vertex does not exist then we create it here
		if t not in self.vertList:
			nv = self.addVertex(t)				#if the to vertex oes not exist then we create it here
		self.vertices[f].addnbr(self.vertices[t], cost)		#this calls the add neighbour method from the vertex class

		

	def getvertices():
		return self.vertices.keys()


	def __contains__(self,n):
		return n in self.vertList
        										#still dicey and not clear about what these two do 
        										#get back to it eventually

	def __iter__(self):
		return iter(self.vertList.values())









