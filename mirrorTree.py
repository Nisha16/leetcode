
INT_MAX = float("infinity")
INT_MIN = float("-infinity")

class BST:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

	def isMirror(self, root1, root2):
		if root1 is None and root2 is None:
			return True
		if root1 is not None and root2 is not None:
			if root1.data == root2.data:
				#return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))
				#print "tree1: ", root1.data , "and " + "tree2: ", root2.data
				return (self.isMirror(root1.left, root2.left) and self.isMirror(root1.right, root2.right))
		return False

	def Check_similar(self, root):
		return self.isMirror(root, root)

	def print_at_eachlevel(self,root):
		thislevel = [root]
		while thislevel:
			nextlevel = list()
			for n in thislevel:
				print n.data
				if n.left: nextlevel.append(n.left)
				if n.right: nextlevel.append(n.right)
			print 
			thislevel = nextlevel

	def IsBST(self,root):
		return (self.is_bst_util(root,INT_MIN,INT_MAX))

	def is_bst_util(self,root,mini,maxi):
		if root is None:
			return True
		if root.data < mini or root.data > maxi:
			return False
		return (self.is_bst_util(root.left,mini,root.data -1) and self.is_bst_util(root.right, root.data + 1, maxi))

	def maxDepth(self,root):
		if self.root == None:
			return 0

		return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1	

	def if_subtree_otherTree(self, main_tree, sub_tree):
		if sub_tree is None:
			return None

		if main_tree is None:
			return None

		if (self.isMirror(main_tree, sub_tree)):
			return True

		return self.if_subtree_otherTree(main_tree.left, sub_tree) or self.if_subtree_otherTree(main_tree.right, sub_tree)							




T = BST(26)
T.right = BST(3)
T.right.right  = BST(3)
T.left = BST(10)
T.left.left = BST(4)
T.left.left.right = BST(30)
T.left.right = BST(6)

S = BST(10)
S.right = BST(6)
S.left = BST(4)
S.left.right = BST(30)

root = BST(5)
root.left = BST(4)
root.right = BST(7)
root.left.left = BST(2)
#root.left.right = BST(3)
root.right.left = BST(6)
root.right.right = BST(9)



print T.if_subtree_otherTree(T, S)

# root.print_at_eachlevel(root)
# print "ISBST: ", root.IsBST(root)
# mirrorTree = BST(1)
# mirrorTree.left = BST(2)
# mirrorTree.right = BST(2)
# mirrorTree.left.left = BST(3)
# mirrorTree.left.right = BST(4)
# mirrorTree.right.left = BST(4)
# mirrorTree.right.right = BST(5)
# mirrorTree.right.right.right = BST(5)
# print "1" if root.isMirror(root,mirrorTree) == True else "0"  						