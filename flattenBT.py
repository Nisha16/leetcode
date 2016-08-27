class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root != None:
            if root.left != None:
                root = root.right
            else:
                temp = root.left
                while temp.right != None:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None