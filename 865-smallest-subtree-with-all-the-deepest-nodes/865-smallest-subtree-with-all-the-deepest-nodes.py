# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.ReturnNode = None
        self.MaxDepth = 0
        
        def dfs(node,depth):
            if node is None:
                self.MaxDepth = max(depth,self.MaxDepth)
                return depth
            
            left = dfs(node.left,depth+1)
            right = dfs(node.right,depth+1)
            
            if left == right == self.MaxDepth:
                self.ReturnNode = node
            return max(left,right)
        
        dfs(root,1)
        return self.ReturnNode
        