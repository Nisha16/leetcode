import collections

class BinarySearch:
	def __init__(self, root):
		self.root = root
		self.left = None
		self.right = None

	def __repr__(self):
		return 'Node with data %d' % self.root
		
	def insert(self, data):
		if self.root:
			if data < self.root:
				if self.left == None:
					self.left = BinarySearch(data)
				else:
					self.left.insert(data)
			else:
				if self.right == None:
					self.right = BinarySearch(data)
				else:
					self.right.insert(data)
		else:
			self.root = data
	def lookup(self, data, parent=None):
		if data < self.root:
			if self.left is None:
				return None, None
			else:
				return self.left.lookup(data, self)
		elif data > self.root:
			if self.right is None:
				return None, None
			else:
				return self.right.lookup(data, self)
		else:
			return self, parent

	def children_count(self):
		count = 0
		if self.left:
			count += 1
		if self.right:
			count += 1
		return count

	def descendant_count(self):
		count =0
		if self.left:
			count += 1 + self.left.descendant_count()
		if self.right:
			count += 1 + self.right.descendant_count()
		return count

	def delete(self,data):
		node, parent = self.lookup(data)
		if node:
			children_count = node.children_count()
			if children_count == 0:
				# If node has no children then remove it
				if parent.left == None:
					parent.left = None
				else:
					parent.right = None
				del node	
			elif children_count == 1:
				if node.left:
					child = node.left
				else:
					child = node.right
				if parent:
					if parent.left is node:
						parent.left = child
					else:
						parent.right = child
				del node		
			else:
				parent = node
				successor = node.right
				while successor.left:
					parent = successor
					successor = successor.left
				node.data = successor.data
				if parent.left == successor:
					parent.right = successor.right
				else:
					parent.right = successor.right

	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print self.data
		if self.right:
			self.right.print_tree()

# """kth smallest element reverse inorder traversal"""			


	def kthlargest(self, node, k, count):
		# count = []
		if node is None:
			return None

		#kth_largest = BinarySearch(None)

		kth_largest = self.kthlargest(node.right, k, count)

		if kth_largest == None:
			print "count: ", count
			count[0] += 1
			if count[0] == k:
				kth_largest = node

		if kth_largest == None:
			kth_largest = self.kthlargest(node.left, k, count)

		print "kthlargest: ", kth_largest		

		return kth_largest

	def kthsmallest(self, node, k, count):
		
		#count = [0]

		if node == None:
			return None

		kth_smallest = self.kthsmallest(node.left, k, count)
		
		if kth_smallest	== None:
			print "count: ", count
			count[0] += 1
			if count[0] == k:
				kth_smallest = node

		if kth_smallest == None:
			kth_smallest = self.kthsmallest(node.right, k, count)	

		print "kthsmallest: ", kth_smallest	

		return kth_smallest	

def minimal_BST(list_of_nodes):
	
	return minimal_height_BST(list_of_nodes, 0, (len(list_of_nodes) - 1))

def minimal_height_BST(list_of_nodes, start, end):
	if start > end:
		return None

	mid = (start + end) // 2

	node = BinarySearch(list_of_nodes[mid])

	node.left = minimal_height_BST(list_of_nodes, start, mid - 1)

	node.right = minimal_height_BST(list_of_nodes, mid + 1, end)

	return node

def closest_node(tree, target):
	gap = float("inf")
	closest = tree

	while tree:
		if abs(tree.root - target) < gap:
			gap = abs(tree.root - target)
			closest = tree
		if target == tree.root:
			break
		elif target < tree.root:
			tree = tree.left
		else:
			tree = tree.right

	return closest.root	

def elements_X_to_Y(tree, X, Y):
	if tree is None:
		return None
	if X < tree.root:
		elements_X_to_Y(tree.left, X, Y) 
	if X <= tree.root and Y >= tree.root:
		print tree.root , " "
	if Y > tree.root:
		elements_X_to_Y(tree.right, X, Y)		
			

		
			
root = BinarySearch(12)
root.insert(2)
root.insert(3)
root.insert(1)
root.insert(5)
root.insert(6)
root.insert(8)
root.insert(11)
root.insert(9)
#print root.lookup(4)

# print root.kthsmallest(root, 5)	

# print "efficient"
# k = 6
# count = [0]

# #print root.kthlargest(root,2, count)

# print root.kthsmallest(root, 9, count)

nodes = [1,2,3,4,5,6,7,8]

#g = BinarySearch(0)
print minimal_BST(nodes)

print "closest node: ", closest_node(root, 7)

elements_X_to_Y(root, 4, 11)




				
				
				
				


					
					
					
					

		