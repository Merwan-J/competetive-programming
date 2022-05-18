"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
#       RECUSIVE SOLUTION         

#         visited = []
#         def dfs(node):
#             if node not in visited:
#                 visited.append(node)
#             depth = 0
#             for child in node.children:
#                 if child not in visited:
#                     depth = max(dfs(child),depth)
            
#             return depth + 1
        
#         return dfs(root) if root is not None else 0

#       ITERATIVE SOLUTION

        if root is None:
            return 0
        
        visited = []
        stack = [(root,1)]
        depth = 0
        
        while stack:
            node,val = stack.pop()
            if node not in visited:
                visited.append(node)
            
            depth = max(depth,val)
            
            for child in node.children:
                if child not in visited:
                    stack.append((child,val+1))
                
        return depth         
        
                    
