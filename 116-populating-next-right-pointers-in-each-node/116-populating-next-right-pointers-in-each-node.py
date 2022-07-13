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
#         q = collections.deque([root])
        
#         if root:
#             while q:
#                 temp = []
#                 while q:
#                     node = q.popleft()
#                     if node:
#                         if q:
#                             node.next = q[0]
#                         temp += [node.left,node.right]
#                 q = collections.deque(temp)
        
        
#         return root

        cur,nxt = root,root.left if root else None
        
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        
        return root
                    