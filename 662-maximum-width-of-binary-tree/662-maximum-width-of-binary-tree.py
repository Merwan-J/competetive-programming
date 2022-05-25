# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def friends(node,i):
            if node is None:
                return []
            ans = []
            
            if node.left: ans.append((node.left,2*i))
            if node.right: ans.append((node.right,2*i+1))
            return ans
        
        dq = collections.deque([(root,1)])
        temp = collections.deque([])
        width = 1
        
        while dq:
            v = dq.popleft()
            
            for node in friends(v[0],v[1]):
                temp.append(node)
                
            if not dq and temp:
                l = temp[0][1]
                r = temp[-1][1]
                width = max(width,r-l+1)
                
                dq = collections.deque(temp)
                temp = collections.deque([])
                
        return width
            
                    