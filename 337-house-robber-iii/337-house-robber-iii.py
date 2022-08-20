# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node,canRob):
            if node is None:
                return 0
            left = node.left 
            right = node.right 
            
            rob = node.val + dfs(node.right,False) + dfs(node.left,False) if canRob else 0
            noRob = dfs(node.right,True) + dfs(node.left,True)
            return max(rob,noRob)
        
        return dfs(root,True)
