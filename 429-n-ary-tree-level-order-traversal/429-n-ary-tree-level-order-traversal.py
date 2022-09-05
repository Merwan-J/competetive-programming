"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = deque([])
        ans = []
        if root:
            ans.append([root.val])
            q.append(root)
        
        while q:
            temp = []
            while q:
                node = q.popleft()
                temp+=[n for n in node.children]
            q = deque(temp)
            if temp:
                ans.append([node.val for node in temp])
        
        return ans
            
        