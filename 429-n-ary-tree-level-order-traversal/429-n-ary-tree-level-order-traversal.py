"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        dq = collections.deque([root])
        ans = [[root.val]]
        while dq:
            
            temp = collections.deque([])
            tempval = []
            while dq:
                v = dq.popleft()
                for node in v.children:
                    temp.append(node)
                    tempval.append(node.val)
            if temp:
                ans.append(tempval)
                dq = collections.deque(temp)
        
        return ans
                