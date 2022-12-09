# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,mx,mn):
            if node is None:
                return 0
            
            left = dfs(node.left,max(mx,node.val),min(mn,node.val))
            right = dfs(node.right,max(mx,node.val),min(mn,node.val))
            
            return max(abs(node.val-mx),abs(node.val-mn),left,right)
        
        return dfs(root,root.val,root.val)