# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        
        graph = defaultdict(list)
        self.startNode = None
        
        
        def buildGraph(node):
            if node is None:
                return 
            
            if node.val == start:
                self.startNode = node 
            
            graph[node]+=[node.right,node.left]
            graph[node.right].append(node)
            graph[node.left].append(node)
            
            buildGraph(node.right)
            buildGraph(node.left)
        
        
        buildGraph(root)
        
        q = [self.startNode]
        level = 0 
        visited = set()
        
        while q:
            n = len(q)
            curQueue = []
            
            for _ in range(n):
                node = q.pop()
                visited.add(node)
                
                for friend in graph[node]:
                    if friend not in visited and friend is not None:
                        curQueue.append(friend)
            q = curQueue
            level += 1
        
        return level - 1
                