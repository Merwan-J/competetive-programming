# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node,l,r):
            if node is None:
                return True
            
            if node.val<=l or node.val>=r:
                return False
            
            return dfs(node.left,l,node.val) and dfs(node.right,node.val,r)
        
        return dfs(root,-inf,inf)