# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = root
        q = deque([(root,0)])
        
        while q:
            n = len(q)
            cur = (inf,None)
            # print([node.val,d for node,d in q])
            for _ in range(n):
                node,pos = q.popleft() 
                if pos<cur[0]:
                    cur = (pos,node)
                if node.left:
                    q.append((node.left,pos-1))
                if node.right:
                    q.append((node.right,pos+1))
            ans = cur[1]
        
        return ans.val