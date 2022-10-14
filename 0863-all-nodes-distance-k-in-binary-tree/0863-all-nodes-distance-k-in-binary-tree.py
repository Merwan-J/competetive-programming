# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent = dict()
        
        
        def findParent(node,prev):
            if node is None:
                return 
            parent[node] = prev
            
            findParent(node.right,node)
            findParent(node.left,node)
        findParent(root,None)
        level = 0
        q = deque([target])
        ans = []
        visited = set()
        
        while q and level<=k:
            # print([node.val if node else None for node in q])
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                
                if node is None or node in visited: continue
                
                visited.add(node)
                
                if level == k:
                    ans.append(node.val)
                q.append(node.right)
                q.append(node.left)
                q.append(parent[node])
                
            level+=1
            
        
        return ans
        
            
        