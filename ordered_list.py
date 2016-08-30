from node import Node 

class OrderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		self.head = None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
		
	def add(self,item):
		temp = Node(item)
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current) 
			previous.setNext(temp)
			


	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current !=None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found
		
	def remove(self,item):
		current = self.head
		previous = None
		stop = False
		found = False
		while current != None and not stop and not found:
			if current.getData() == item:
				if previous == None:
					self.head = current.getNext()
				else:
					previous.setNext(current.getNext())
				found = True
			elif current.getData() > item:
				stop = True
			else:
				current = current.getNext()
		return found

	def display(self):
		current = self.head
		while current != None:
			print (current.getData())
			current = current.getNext()
		
	
mylist = OrderedList()
mylist.add(16)
mylist.add(24)
mylist.add(6)
mylist.add(30)
mylist.display()
print mylist.search(24)
print mylist.search(22)
print mylist.remove(16)
print mylist.size()
mylist.display()	

				


					

					
				
				

				
					
					

			
		
		