# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        ans = []
        if root is None:
            return ans
        
        while q:
            ans.append(q[-1].val)
            temp = []
            while q:
                node = q.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            q = collections.deque(temp)
        
        return ans
            
            
            
            
                
            
            