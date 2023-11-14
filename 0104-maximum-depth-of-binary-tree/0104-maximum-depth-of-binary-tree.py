# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
            
                    
        q = [root]
        level = 0 
        
        while q:
            n = len(q)
            children = []
            
            for _ in range(n):
                node = q.pop()
                if node.right: children.append(node.right)
                if node.left: children.append(node.left)
            q = children 
            level+=1
        
        return level
        
        