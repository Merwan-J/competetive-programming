# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
                
            self.sum += abs(left-right)
            
            return node.val + left + right
        
        helper(root)
        return self.sum