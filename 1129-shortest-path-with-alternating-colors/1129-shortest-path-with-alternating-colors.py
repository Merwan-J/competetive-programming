class Solution:
    def shortestAlternatingPaths(self, n: int, red: List[List[int]], blue: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]
        ans = [-1]*n
        visited = set()
        
        for u,v in red:
            graph[u].append((v,1))
        
        for u,v in blue:
            graph[u].append((v,0))
                    
        q = deque([(0,1),(0,0)])
        level = 0
        
        while q:
            n = len(q)
            for i in range(n):
                node,color = q.popleft()
                
                if ans[node] == -1:
                    ans[node] = level
                    
                visited.add((node,color))
                
                for adj in graph[node]:
                    if adj[1]!=color and adj not in visited:
                        q.append(adj)
                
            level+=1
        
        return ans
                