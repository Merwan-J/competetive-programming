"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return 
        
        dummyNode = Node(0) 
        cur = dummyNode
        stack = [head] 
        
        while stack:
            tempNode = stack.pop()
            
            if tempNode.next:
                stack.append(tempNode.next)
            if tempNode.child:
                stack.append(tempNode.child)
            
            cur.next = tempNode
            tempNode.prev = cur
            cur.child = None
            cur = tempNode 
        
        root = dummyNode.next 
        root.prev = None
        
        return root 