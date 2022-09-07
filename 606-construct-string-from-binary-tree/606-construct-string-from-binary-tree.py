# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if node is None:
                return "()"
            
            if node.right is None and node.left is None:
                return str(node.val) if node is root else "("+str(node.val)+")"
            
            left = dfs(node.left)
            right = dfs(node.right)
            if right == "()": right=""
                
            ans = str(node.val)+left+right if node is root else "("+str(node.val)+left+right+")" 
            
            return ans
        
        return dfs(root)