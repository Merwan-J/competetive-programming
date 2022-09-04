# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = defaultdict(list)
        
        def dfs(node,row,col):
            if node is None:
                return
            
            hmap[col] += [(row,node.val)]
            dfs(node.right,row+1,col+1)
            dfs(node.left,row+1,col-1)
        dfs(root,0,0)
        hmap = sorted(hmap.items())
        hmap = [items[1] for items in hmap]
        temp = [sorted(item) for item in hmap]
        ans = []
        for items in temp:
            t = []
            for item in items:
                t.append(item[1])
            ans.append(t)
        print(ans)
        
        return [vals for vals in ans] 