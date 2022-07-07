# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def helper(node):
            if node is None:
                return (0,0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            sum = left[0]+right[0]+node.val
            count = left[1]+right[1]+1
            avg = sum//count
            
            if avg == node.val:
                self.count += 1
            return sum,count
        
        helper(root)
        return self.count