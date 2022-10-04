class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:        
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for node,val in enumerate(bombs):
            x,y,r1 = val
            for adj,val in enumerate(bombs):
                a,b,r2 = val
                if node!=adj:
                    d = sqrt((x-a)**2 + (y-b)**2)
                    if d<=r1:
                        graph[node] +=[adj]
                
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            ans = 1
            
            for adj in graph[node]:
                if adj not in visited:
                    ans += dfs(adj)
            
            return ans
        
        count = 0
        for node in range(n):
            visited = set()
            count = max(count,dfs(node))
        
        return count
            
            
                    
                        