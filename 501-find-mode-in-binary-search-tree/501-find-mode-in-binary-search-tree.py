# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = defaultdict(int)
        
        def dfs(node):
            if node is None:
                return
            
            nodes[node.val] += 1
            
            dfs(node.right)
            dfs(node.left)
        
        dfs(root)
        nodes = sorted(nodes.items(),key=lambda item: item[1],reverse=True)
        
        modes = []
        maxMode = 0 
        
        for val,mode in nodes:
            if mode >= maxMode:
                maxMode = mode
                modes.append(val)
        
        return modes
        
        