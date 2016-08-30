 class BinaryTree:
	def __init__(self,root):
		self.key = root
		self.left = None
		self.right = None

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self,newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

	def getright(self):
		return self.right

	def getleft(self):
		return self.left

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print self.key + ' '
		if self.right:
			self.right.PrintTree()

	def PreOrder(self):
		print self.key
		if self.left:
			self.left.PreOrder()
		if self.right:
			self.right.PreOrder()

	def inOrder(self):
		if self.left:
			self.left.inOrder()
		print self.key
		if self.right:
			self.right.inOrder()

	def postOrder(self):
		if self.left:
			self.left.postOrder()
		if self.right:
			self.right.postOrder()
		print self.key	


# if any sub trees are identical
inordersubtree = []

def get_inorder_subtrees(tree):

	global inordersubtree

	if (tree.left is None) and (tree.right is None):
		return tree.key

	temp = ''
	
	if tree.left is not None:
		temp = get_inorder_subtrees(tree.left)

	temp = temp + tree.key
	
	if tree.right is not None:
		temp = temp + get_inorder_subtrees(tree.right)

	inordersubtree.append(temp)
	
	return temp			

postordersubtree = []

def get_postorder_subtrees(tree):

	global postordersubtree

	if (tree.left is None) and (tree.right is None):
		return tree.key

	temp = ''
	
	if tree.left is not None:
		temp = get_postorder_subtrees(tree.left)

	if tree.right is not None:
		temp = temp + get_postorder_subtrees(tree.right)

	temp = temp + tree.key
	
	postordersubtree.append(temp)

	return temp

#Lowest common ancestor for two nodes

def find_path(root, path, k):
	if root is None:
		return False

	# Store this node is path vector. The node will be
	# removed if not in path from root to k
	path.append(root.key)

	# See if the k is same as root's key
	if root.key == k:
		return True

	# Check if k is found in left or right sub-tree
	if ((root.left != None and find_path(root.left, path, k)) or
	(root.right!= None and find_path(root.right, path, k))):
		return True

	# If not present in subtree rooted with root, remove
	# root from path and return False
	path.pop()
	return False

def findLCA(root, n1, n2):
	# To store paths to n1 and n2 fromthe root

	path1 = []
	path2 = []

	# Find paths from root to n1 and root to n2.
	if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
		return -1

	# Compare the paths to get the first different value
	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]

def mirror(root):
	if root is None:
		return None
	mirror(root.left)
	mirror(root.right)
	root.left, root.right = root.right, root.left
	return root	

def isBalanced(tree):
	return isBalancedTree(tree)>=0

def isBalancedTree(tree):
	if tree is None:
		return None

	left = isBalancedTree(tree.left)	
	right = isBalancedTree(tree.right)

	if left<0 or right<0 or abs(left-right)>1:
		return -1
	return max(left,right)+1	



root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

					
r = BinaryTree('a')
# print r.getRootVal()
#print r.getleft()
r.insertLeft('b')
r.insertLeft('d')
r.insertLeft('g')
#print(r.getleft())
# print r.getleft().getRootVal()
r.insertRight('c')
r.insertRight('b')
r.insertRight('d')
r.insertRight('g')
#print(r.getright())
#print r.getright().getRootVal()
# r.getright().setRootVal('hello')
#print r.getright().getRootVal()
print 'preorder', root.PreOrder()

mirror(root)

print 'after: ', root.PreOrder()
# print 'Inorder', r.inOrder()
# print 'PostOrder', r.postOrder()

# print get_inorder_subtrees(r)

# print get_postorder_subtrees(r)

# dic = {}

# print inordersubtree

# print postordersubtree

# for inorder, postorder in zip(inordersubtree, postordersubtree):
# 	if inorder + "-" + postorder in dic:
# 		print "Duplicate Subtrees present"
# 	else:
# 		dic[inorder + "-" + postorder] = "Tree"
# 		print "Binary tree has all unique subtrees"	

# print dic

print findLCA(root,4,5)

print isBalanced(root)





			
			
			


