"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        visited = dict()
        
        def helper(node,count):
            visited[node] = True
            
            if not node.children:
                return count
            depth = 0
            for vertex in node.children:
                if vertex not in visited:
                    depth = max(depth,helper(vertex,count+1))
            return depth
        return helper(root,1)
        
        