# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        def friends(node,turn):
            if node is None:
                return []
            ans = []
            
            if node.left: ans.append(node.left)
            if node.right: ans.append(node.right)
            return ans
        
        dq = collections.deque([root])
        temp = []
        ans = [[root.val]]
        turn = 1
        while dq:
            v = dq.popleft()
            for node in friends(v,turn):
                temp.append(node)
            
            if not dq and temp:
                if turn%2:
                    ans.append([node.val for node in temp][::-1])
                else:
                    ans.append([node.val for node in temp])
                
                dq = collections.deque(temp)
                temp = []
                turn += 1
        return ans