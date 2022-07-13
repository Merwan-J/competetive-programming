"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = collections.deque([root])
        
        if root:
            while q:
                temp = []
                while q:
                    node = q.popleft()
                    if node:
                        if q:
                            node.next = q[0]
                        else:
                            node.next = None
                        temp += [node.left,node.right]
                q = collections.deque(temp)
        
        
        return root
                    