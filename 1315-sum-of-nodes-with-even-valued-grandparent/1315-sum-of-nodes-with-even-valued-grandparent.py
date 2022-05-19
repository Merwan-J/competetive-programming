# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        stack = []
        self.sum = 0
        def dfs(node):
            if node is None:
                return 
            
            stack.append(node)
            if len(stack)-2>0 and stack[len(stack)-3].val%2==0:
                self.sum += node.val
            dfs(node.left)
            dfs(node.right)
            
            stack.pop()
        dfs(root)
        return self.sum
            
        
            