class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def lookup(self,data,parent=None):
		if data < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(data,self)
		elif data > self.data:
			if self.right is None:
				return None, None
			return self.right.lookup(data,self)
		else:
			return self, parent	

	def children_count(self):
		cnt = 0
		if self.left:
			cnt += 1
		if self.right:
			cnt +=1
		return cnt

	def delete(self,data):
		node, parent = self.lookup(data)
		if node is not None:
			children_count = node.children_count()
		if children_count == 0:
			if parent:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			else:
				self.data = None
		elif children_count == 1:
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				del node	
			else:
				self.left = n.left
				self.right = n.right
				self.data = n.data
		else:
			parent = node
			succussor = node.right
			while succussor.left:
				parent = succussor
				succussor = succussor.left
			node.data = succussor.data
			if parent.left == succussor:
				parent.left = succussor.right
			else:
				parent.right = succussor.right

	def compare_trees(self,node):
		if node is None:
			return False
		if self.data != node.data:
			return False
		res = True
		if self.left is None:
			if node.left:
				return False
		else:
			res = self.left.compare_trees(node.left)
		if res is False:
			return False
		if self.right is None:
			if node.right:
				return False
		else:
			res = self.right.compare_trees(node.right)
		return res									

																								


root = Node(24)
root.insert(16)
root.insert(6)
root.insert(10)
root.insert(36)
root.insert(30)
root.insert(22)
node, parent = root.lookup(24)
print "node: ", node ," and " + "parent: ", parent
root1 = Node(24)
root1.insert(16)
root1.insert(6)
root1.insert(10)
root1.insert(36)
root1.insert(20)
root1.insert(22)
print root.compare_trees(root1)



					

					

		