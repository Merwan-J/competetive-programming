# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def friends(node):
            if node is None:
                return []
            ans = []
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return ans
        
        if root is None:
            return []
        dq = collections.deque([root])
        ans = collections.deque([[root.val]])
        temp = []
        
        while dq:
            v = dq.popleft()
            
            for node in friends(v):
                temp.append(node)
            
            if not dq and temp:
                ans.appendleft([node.val for node in temp])
                dq = collections.deque(temp)
                temp = []
        return ans