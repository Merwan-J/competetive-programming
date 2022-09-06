# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return False
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            if right is False:
                node.right = None
            if left is False:
                node.left = None
            
            return node.val==1 or right or left
        
        if dfs(root) is False:
            root = None
        return root