# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def helper(node,total):
            if node is None:
                return False
            
            total+=node.val
            if node.right is None and node.left is None:
                return total == targetSum
            
            left = helper(node.left,total)
            right = helper(node.right,total)
            
            return left or right
        
        return helper(root,0)
                
