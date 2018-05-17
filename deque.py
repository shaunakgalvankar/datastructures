#this is the implementation of the deque ADT

#a deque has the properites of both stack and queues that is items can be added and
#removed from it from both the ends.it doesnt follow FIFO or LIFO
class deque:

	#this is the constructorwhich initialises the an empty deque as a list
	def __init__(self):
		self.deque=[]

	#this adds the element to the right of the head element   
	def addfront(self,x):
		self.deque.append(x)
		return x

	#this adds an element to the lleft of the first element
	def addrear(self,x):
		self.deque.insert(0,x)
		return x

	#returns the number of elements present in the deque
	def size(self):
		return len(self.deque)

	#thsi removes the head element
	def removefront(self):
		return self.deque.pop()

	#this removes the tail element
	def removerear(self):
		return self.deque.pop(0)
		
	#returns a boolean on the basis of the deque is empty or full
	def isempty(self):
		if len(self.deque)==0:
			return True
		else:
			return False


	#this is the demonsrator program
d=deque()
d.addfront(1)
d.addfront(2)
d.addfront(3)
d.addrear(1)
d.addrear(2)
d.addrear(3)
print(d.deque)
d.removerear()
d.removerear()
d.removefront()
d.removefront()
print(d.deque)
print(d.size())
print(d.isempty())