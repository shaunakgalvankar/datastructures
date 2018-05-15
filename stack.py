#this is the implementation of the stack adt


class stack:
	
	#the constructor initialises an empty stack
	def __init__(self):
		self.stack=[]

	#this methods adds an element passed as parameter to the top of the stack
	def push(self,item):	
		return self.stack.append(item)

#this methods removes the element at the top of the stack and return the element that was removed
	def pop(self):
		x=self.stack[-1]
		self.stack.remove(x)
		return x
	#this method returns a boolean value based on if the stack is empty or not
	def isempty(self):
		if (len(self.stack)==0):
			return True

		else:
			return False

	#this method returns the number of elements present on the stack
	def size(self):
		return len(self.stack)+1

	#this method returns the top element 
	def peek(self):
		return self.stack[-1]

	#this method returns the bottom element
	def bottom(self):
		return self.stack[0]

s=stack()				#this creates an object of the stack class that we created and assigns it tot a variable

#the following code demonstrates the working of each method in the stack class with sample values

#run it in your terminal or command prompt to see it work
print(s.isempty())
a=s.push(1)
print(s.stack)
b=s.push(2)
print(s.stack)
c=s.push(3)
print(s.stack)
d=s.push(4)
print(s.stack)
e=s.push(5)
print(s.stack)
f=s.pop()
g=s.size()
h=s.peek()
i=s.bottom()
j=s.isempty()

print(f)
print(g)
print(h)
print(i)
print(j)
