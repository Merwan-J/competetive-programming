class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        q = deque([(0,[0])])
        
        
        while q:
            node,path = q.popleft()
            
            if node == n-1:
                ans.append(path)
            
            for adj in graph[node]:
                q.append((adj,path+[adj]))
        
        return ans
        
        
                