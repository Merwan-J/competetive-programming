# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque([root])
        
        ans = []
        
        while q:
            temp = []
            maxx = float('-inf')
            
            while q:
                node = q.popleft()
                if node.right: temp.append(node.right)
                if node.left: temp.append(node.left)
                maxx = max(node.val,maxx)
            q = deque(temp)
            ans.append(maxx)
        
        return ans
                    