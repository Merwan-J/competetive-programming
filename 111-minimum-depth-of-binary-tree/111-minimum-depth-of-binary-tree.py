# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dfs(node,depth):
            if node.right is None and node.left is None:
                return depth + 1
            left,right = sys.maxsize,sys.maxsize
            
            if node.left:
                left = dfs(node.left,depth+1)
            if node.right:
                right = dfs(node.right,depth+1)
            
            return min(left,right)
        
        return dfs(root,0)