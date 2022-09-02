# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # nodes = defaultdict(list)
        # def dfs(node,depth):
        #     if node is None:
        #         return
        #     nodes[depth]+=[node.val]
        #     dfs(node.right,depth+1)
        #     dfs(node.left,depth+1)
        # depth = 0
        # dfs(root,depth)
        # return[sum(nodes[depth])/len(nodes[depth]) for depth in range(len(nodes))]
        
        q = deque([root])
        ans = []
        
        while q:
            temp = []
            n = 0
            total = 0
            
            while q:
                node = q.popleft()
                total+=node.val
                n+=1
                if node.right: temp.append(node.right)
                if node.left: temp.append(node.left)
            ans.append(total/n)
            q = deque(temp)
        
        return ans
        