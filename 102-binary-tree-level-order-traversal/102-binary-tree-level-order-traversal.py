# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
        ans = [[root.val]]
        temp = []
        tempval = []
        while dq:
            v = dq.popleft()
            
            for node in friends(v):
                temp.append(node)
                tempval.append(node.val)
            
            if not dq and temp:
                ans.append(tempval)
                dq = collections.deque(temp)
                temp,tempval = [],[]
        return ans
            
            