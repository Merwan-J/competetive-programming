# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if root is None:
            return arr
        
        def helper(node):
            if node.left is None and node.right is None:
                arr.append(node.val)
                return None
            
            if node.left:
                helper(node.left)
            
            arr.append(node.val)
            
            if node.right:
                helper(node.right)
        
        helper(root)
        return arr