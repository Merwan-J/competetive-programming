# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node,target):
            if node is None:
                return 
            
            left = dfs(node.left,target)
            right  = dfs(node.right,target)
            
            count  = (left in target) + (right in target) + (node in target)
            
            if count == 2:
                self.ans = node
                return  
            
            if left in target:
                return left
            if right in target:
                return right
            if node in target:
                return node
            return None
        
        dfs(root,[p,q])
        return self.ans
            
            