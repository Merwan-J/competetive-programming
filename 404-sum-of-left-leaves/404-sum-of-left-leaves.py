# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,left):
            if node is None:
                return 0
            if node.right is None and node.left is None:
                return node.val if left else 0
            
            return dfs(node.left,True) + dfs(node.right,False)
        
        return dfs(root,False)