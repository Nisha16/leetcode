#from node import Node

class Node (object):
	def __init__(self,initdata,next = None):
		self.data = initdata
		self.next = next

def create_list():
	last = Node(8)
	head = Node(7,last)
	head = Node(6,head)
	head = Node(5,head)
	head = Node(4,head)
	head = Node(3,head)
	head = Node(2,head)
	head = Node(1,head)
	last.next = head
	return head

def is_cycleexists(head):
	slow = head
	fast = head
	while fast != None:
		slow = slow.next
		if slow is fast:
		 	return True
		if fast.next != None:
		 	fast = fast.next.next
		else:
		 	return False
		if slow is fast:
		 	return True
	return False
		 
def detect_cycle(head):
	tortoise = head
	hare = head
	while hare:
		tortoise = tortoise.next
		hare = hare.next
		if hare:
			hare = hare.next
			if tortoise is hare:
				print "T: ", tortoise.data
				return True
	print "T: ", tortoise.data			
	return False


def getMiddleElement(head):
	slow = head
	fast = head
	while fast != None and fast.next != None:
		fast = fast.next.next
		slow = slow.next
	return slow.data

# def reverse_list(head):
# 	new_head = None
# 	while head:
# 		new_head = Node(head.value, new_head)
# 		head = head.next
# 	return new_head

def reverse_list1(head):
	current = head
	previous = None
	while current:
		next1 = current.next
		current.next = previous
		previous = current
		current = next1
	head = previous	

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None		


			

				
node = create_list()
#print detect_cycle(node)
#print "Mid element: ", getMiddleElement(node)
display(node)
#new_ll = reverse_list(node)
print "first list"
#display(node)
print "seconf list"
#display(new_ll)

		 		
		 		
		 		

		
		