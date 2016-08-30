class Node(object):
	def __init__ (self,initdata,next = None):
		self.data = initdata
		self.next = next

def create_list():

	fifth = Node(9,None)
	fourth = Node(10,fifth)
	third = Node(7,fourth)
	second = Node(8, third)
	first = Node(5,second)
	head = Node(2,first)
	# first = Node(5,second)
	# second = Node(9, third)
	# third = Node(7,fourth)
	# fourth = Node(10,None)
	return head

def print_list(head):
	current = head
	#print "first"
	while current is not None:
		print current.data
		current = current.next

def remove_duplicate(head):
	if head is None:
		return head
	dup_set = set()
	dup_set.add(head.data)
	current = head
	while current.next != None:
		if current.next.data in dup_set:
			current.next = current.next.next
		else:
			dup_set.add(current.next.data)
			current = current.next
	return head

def delete_key(head,key):
	previous = None
	current = head

	while current is not None:
		if key == current.data:
			break
		previous = current
		current = current.next

	if current == None:
		return head

	if current == head:
		return current.next

	previous.next = current.next

	return head	

def intersect(head1,head2):
	list1node = None
	list1length = getlength(head1)
	list2node = None
	list2length = getlength(head2)

	length_difference = 0

	if list1length >= list2length:
		length_difference = list1length - list2length
		list1node = head1
		list2node = head2
	else:
		length_difference = list2length - list1length
		list1node = head2
		list2node = head1

	while length_difference > 0:
		list1node = list1node.next
		length_difference -= 1

	while list1node is not None:
		if list1node == list2node:
			return list1node

		list1node = list1node.next
		list2node = list2node.next

		return None

def getlength(head):
	count = 0
	current = head
	while current is not None:
		count += 1
		current = current.next

	return count
	
def find_nth_from_last(head,n):
	if head is None and n < 1:
		return None

	tail = head
	
	while tail != None and n > 0:
		tail = tail.next
		n -= 1

	#to check out of bounds
	if n != 0:
		return None

	while tail != None:
		tail = tail.next
		head = head.next

	return head

def swap_nth_node(head,n):
	previous = None
	current = head

	if head == None:
		return head
	if n == 1:
		return head

	count = 1
	while current is not None and count < n:
		previous = current
		current = current.next
		count += 1

	if current == None:
		return head

	previous.next = head
	temp = head.next
	head.next = current.next
	current.next = temp

	return current	

def merge_list(head1, head2):
	if head1 == None:
		return head2
	if head2 == None:
		return head1

	mergeHead = None
	
	if head1.data <= head2.data:
		mergeHead = head1
		head1 = head1.next
	else:
		mergeHead = head2
		head2 = head2.next

	mergeTail = mergeHead
	
	while head1 != None and head2 != None:
		temp = None
		if head1.data <= head2.data:
			temp = head1
			head1 = head1.next
		else:
			temp = head2
			head2 = head2.next

		mergeTail.next = temp
		mergeTail = temp

	if head1 != None:
		mergeTail = head1
	if head2 != None:
		mergeTail = head2

	return mergeHead
	
def adjust_rotations_needed(n,length):
	
	n = n % length

	if n < 0:
		n = n + length

	return n
	
def rotate_list(head, n):
	
	if head == None and n == 0:
		return 

	length = getlength(head)
	
	n = adjust_rotations_needed(n, length)

	if n == 0:
		return head

	rotations_count = length - n - 1
	temp = head	

	while rotations_count > 0:
		rotations_count -= 1
		temp = temp.next

	new_head = temp.next
	
	temp.next = None
	temp = new_head

	while temp.next != None:
		temp = temp.next

	temp.next = head
	
	return new_head	

def rotateList(head, k):
	if k == 0:
		return 
	current = head
	count = 1

	while count < k and current is not None:
		current = current.next
		count += 1

	if current is None:
		return 

	KthNode = current

	while current.next is not None:
		current = current.next

	current.next = head
	head = KthNode.next
	KthNode.next = None				

def reverse(self):
    if self.head:
        prev = None
        current = self.head
        while current:
            future = current.next
            current.next = prev
            prev = current
            current = future
        self.head = prev

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        for __ in range(m - 1):
            node = node.next
        prev = node.next
        curr = prev.next
        for __ in range(n - m):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node.next.next = curr
        node.next = prev
        return dummy.next        

						 

node = create_list()
print_list(node)
#remove_duplicate(node)
#delete_key(node,9)
rotateList(node, 4)
print "After rotating"
print_list(node)




		
