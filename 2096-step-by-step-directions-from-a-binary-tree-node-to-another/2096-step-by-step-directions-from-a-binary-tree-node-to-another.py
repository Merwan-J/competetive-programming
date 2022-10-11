# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath,destPath = "",""
        path = []
        def dfs(node):
            nonlocal startPath,destPath
            if node is None:
                return
            
            if node.val == startValue:
                startPath = "".join(path)
            if node.val == destValue:
                destPath = "".join(path)
            path.append("R")
            dfs(node.right)
            path.pop()
            path.append("L")
            dfs(node.left)
            path.pop()
        
        dfs(root)
        
        i = 0
        while i<min(len(startPath),len(destPath)) and startPath[i] == destPath[i]:
            i+=1
        
        startPath = startPath[i:]
        destPath = destPath[i:]
        
        startPath = "".join(["U" if i == "L" or i =="R" else i for i in startPath])
        
        return startPath+destPath
        
        
        
        