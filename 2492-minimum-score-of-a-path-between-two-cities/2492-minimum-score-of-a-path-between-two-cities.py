class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        
        since I can include roads multiple times in my path, 
        I can basically take the shortest distance between any two cities, 
        given that I reached there starting from node 1
        
        
        
        inorder to find the shortest I can explore everynode starting from node 1
        then visiting only non-visited nodes and there I track the distances then returning           the minimum of them 
        
        
        """
        
        
        graph = [[] for _ in range(n+1)]
        
        for a,b,distance in roads:
            graph[a].append((b,distance))
            graph[b].append((a,distance))
        
        ans = inf
        visited = set()
        
        q = deque([1])
        
        while q:
            node = q.popleft()
            
            if node in visited:
                continue 
            
            visited.add(node)
            
            for adj,distance in graph[node]:
                ans = min(ans,distance)
                if adj not in visited:
                    q.append(adj)
        
        return ans