# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        ans = 0
        def dfs(node):
            nonlocal ans

            if node.right == node.left == None:
                ans = max(ans,node.val)
                return True,node.val,node.val,node.val
            
            bst = False
            cur = 0

            lbs,lsum,ll,lr = dfs(node.left) if node.left else (True,0,inf,-inf)
            rbs,rsum,rl,rr = dfs(node.right) if node.right else (True,0,inf,-inf)
            
            # print(node.val)
            # print(lbs,lsum,ll,lr)
            # print(rbs,rsum,rl,rr)
            # print(lbs and rbs and lr<node.val and node.val<rl)
            # print("--------")
            
            if lbs and rbs and lr<node.val and node.val<rl:
                if node.right and node.left:
                    cur = node.val + lsum + rsum
                    bst = True
                elif node.right and not node.left:
                    cur = node.val + rsum
                    bst = True
                elif node.left and not node.right:
                    cur = node.val + lsum
                    bst = True
                ans = max(ans,cur)
                
            return bst,cur,min(ll,rl,node.val), max(lr,rr,node.val)

        dfs(root)
        return ans