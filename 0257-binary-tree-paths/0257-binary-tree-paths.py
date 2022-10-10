# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        path = []
        
        def dfs(node): 
            if node is None:
                return 
            
            path.append(str(node.val))
            if node.right == node.left == None:
                ans.append("->".join(path))
                path.pop()
                return
            dfs(node.right)
            dfs(node.left)
            path.pop()
            
        dfs(root)
        return ans