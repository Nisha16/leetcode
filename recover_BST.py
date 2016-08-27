# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    prev = None
    p1 = None
    p2 = None
    
    def inOrder(self, root):
        if root == None:
            return
        
        else:
            self.inOrder(root.left)
            if self.prev == None:
                self.prev = root
            else:
                if root.val <= self.prev.val:
                    if self.p1 == None:
                        self.p1 = self.prev
                    self.p2 = root
                self.prev = root
            self.inOrder(root.right)
            return
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.p1 = None
        self.p2 = None
        self.inOrder(root)
        temp = self.p1.val 
        self.p1.val = self.p2.val
        self.p2.val = temp
        return root


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        originalRoot, stack = root, []
        prev = first = second = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev and root.val < prev.val:
                    if first == None:
                        first, second = prev, root
                    else:
                        second = root
                prev, root = root, root.right
        first.val, second.val = second.val, first.val
        return originalRoot        