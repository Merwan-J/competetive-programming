# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        path = []
        def dfs(node):
            nonlocal total
            
            if node is None:
                return
            
            path.append(str(node.val))
            
            if node.right == node.left == None:
                total+=int("".join(path))
            
            dfs(node.right)
            dfs(node.left)
            path.pop()
        
        dfs(root)
        
        return total