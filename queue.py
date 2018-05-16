#this is the implementatio of a queue ADT

class Queue:

	#this constructor initialises an empty queue 
	def __init__(self):
		self.queue=[]

	#this method adds the passed parameter in the rear of the queue	
	def enqueue(self,x):
		self.queue.insert(0,x)
		return self.queue

	#this method removes the element in the fron of the queue
	def dequeue(self):
		self.queue.pop()

	#this method return the front element of the queue
	def showfront(self):
		return self.queue[-1]

	#this method return the rear element of the queue
	def showrear(self):
		return self.queue[0]

	#this method return a booloean to tell if there are ay elements present in the queue
	def isempty(self):
		if (len(self.queue)==0):
			return True
		else:
			return False

	#this method prints the number of elements present in the queue
	def size(self):
		return len(self.queue)

	#this method empties the queue and removes all the elements
	#such type of an application is observed when a jump instruction is faced in the queues of the processor
	def flush(self):
		self.queue=[]
		return self.queue


#demonstrator program
q=Queue()
q.enqueue(1)
print(q.queue)
q.enqueue(2)
print(q.queue)
q.enqueue(3)
print(q.queue)
q.enqueue(4)
print(q.queue)

q.dequeue()
q.dequeue()
print(q.queue)

a=q.showfront()
print(a)
b=q.showrear()
print(b)
c=q.isempty()
print(c)
d=q.size()
print(d)

q.flush()
c=q.isempty()
print(c)


