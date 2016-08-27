class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.postorderTraversalRec(root, result)
        return result
    def postorderTraversalRec(self, root, result):
        if root == None:
            return []
        self.postorderTraversalRec(root.left, result)
        self.postorderTraversalRec(root.right, result)
        result.append(root.val)

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        solution = []
        used = set()
        stack = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node in used:
                solution.append(node.val)
            else:
                used.add(node)
                stack.append(node)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return solution
