from node import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
    	self.head = None

    def add(self,item):
    	temp = Node(item)
    	temp.setNext(self.head)
    	self.head = temp

    def size(self):
    	current = self.head
    	count = 0
    	while (current != None):
    		count = count + 1
    		current = current.getNext()
    	return count
    	
    def search(self,item):
    	current = self.head
    	count = 0
    	found = False
    	while current !=None and not found:
    		count = count + 1
    		if (current.getData() == item):
    			found = True
    		else:
    			current = current.getNext()
    	if found:
    		return "Item found at %d node." % count
    	else:
    		return "Item not found"		

    def remove(self,item):
    	current = self.head
    	previous = None
    	found = False
    	while current != None and not found:
    		if(current.getData() == item):
    			if(previous == None):
    				self.head = current.getNext()
    			else:
					previous.setNext(current.getNext())
    			found = True
    		else:
    			previous = current
    			current = current.getNext()
    	if found:
    		return "The required item is being removed"
    	else:
    		return "Item not found"

    def display(self):
    	current = self.head
    	while current != None:
    		print (current.getData())
    		current = current.getNext()

            


mylist = UnorderedList()
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

    		
    		
    			
    			
    			
    			
    		


    	
        