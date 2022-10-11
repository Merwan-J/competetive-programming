# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.anc = None
        def dfs(node):
            if node is None:
                return False
            
            left,cur,right = False,False,False
            
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node == q or node == p
            
            if cur + right + left == 2:
                self.anc = node
            
            return left or right or cur
        
        dfs(root)
        return self.anc
            
            
                