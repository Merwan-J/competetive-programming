class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = [[] for _ in range(n)]
        time = [inf]*n
        count = [0]*n
        
        
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        
        src,dest = 0,n-1
        heap = [(0,src)]
        count[src] = 1
        time[src] = 0
        
        while heap:
            cost,node = heappop(heap) 
            if node == dest: continue
            for adj,w in graph[node]:
                if cost+w < time[adj]:
                    heappush(heap,(cost+w,adj))
                    count[adj],time[adj] = count[node],cost + w
                    
                elif cost+w == time[adj]:
                    count[adj]+=count[node]
        
        return count[dest]%mod
        
        
        