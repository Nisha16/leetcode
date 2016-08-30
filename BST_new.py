class BSTNode:
	def __init__(self,key,parent=None,left=None,right=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent



class BST:
	def __init__(self):
		self.root = None

	def find_recursively(self,key,node):
		if node == None and key == node.key:
			return node
		elif key < node.key:
			return self.find_recursively(key,node.left)
		else:
			return self.find_recursively(key,node.right)

	def find_iteratively(self,key,node):
		current_node = node
		while current_node:
			if key == current_node.key:
				return current_node
			elif key < current_node:
				current_node = current_node.left
			else:
				current_node = current_node.right

	def search(self,key):
		return self.find_recursively(self.root,key)

	def insert(self,key):
		if self.root == None:
			self.root = BSTNode(key)
			print "count: " , key
			return True
		current_node = self.root
		#print "cur: " , current_node.key
		while current_node:
			if key == current_node.key:
				print "Node already exists"
				return False
			elif key < current_node.key:
				if current_node.left:
					current_node = current_node.left
				else:
					current_node.left = BSTNode(key,current_node)
					print "count: ", key
					return True
			else:
				if current_node.right:
					current_node = current_node.right
				else:
					current_node.right = BSTNode(key,current_node)
					print "count: ", key
					return True

	def print_tree(self):
		if self.root == None:
			print "Tree is empty"
		else:
			current_node = self.root
			while current_node:
				print current_node.key
				if current_node.left:
					current_node = current_node.left
					#print current_node.key
				else:
					current_node = current_node.right

	# def display(self):
	# 	if self.left:
	# 		self.left.display()
	# 	print self.key + ' '
	# 	if self.right:
	# 		self.right.display()

					


	def repalce_node(self,node,new_node):
		if self.root == node:
			self.root = new_node
			return
		parent = node.parent
		if parent.left and parent.left == node:
			parent.left = new_node
		elif parent.right and parent.right == node:
			parent.right = new_node
		else:
			print "Incorrect parent and children relation"
			#raise RuntimeError

	def remove_node(self,node):
		if node.left and node.right:
			succussor = node.right
			while succussor:
				succussor = succussor.left
			node.key = succussor.key
			self.remove_node(succussor)
		elif node.left:
			self.repalce_node(node,node.left)
		elif node.right:
			self.repalce_node(node,node.right)
		else:
			self.repalce_node(node,None)

	def delete(self,key):
		node = self.search(key)
		if node:
			self.remove_node(node)
			
			
								

tree = BST()
tree.insert(6)
tree.insert(4)
tree.insert(9)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(5)	
#tree.delete(10)
#tree.display()	
				
						
				
					
					
					
					
				

		
				
				
				
			
			
			
		   

		    		
		
