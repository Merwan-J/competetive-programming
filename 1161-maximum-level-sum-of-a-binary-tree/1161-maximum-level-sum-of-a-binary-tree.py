# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevelSum = root.val
        maxLevel = 1
        q = [root]
        curLevel = 1
        
        while q:
            n = len(q)
            levelSum = 0
            level = []
            
            for _ in range(n):
                node = q.pop()
                
                levelSum+=node.val
                
                if node.right: level.append(node.right)
                if node.left: level.append(node.left)
                    
            if levelSum>maxLevelSum:
                maxLevelSum = levelSum
                maxLevel = curLevel
                
            q = level
            curLevel+=1
        
        return maxLevel