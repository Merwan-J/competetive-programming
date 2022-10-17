class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = [inf]*(n+1)
        graph = [[] for _ in range(n+1)]
        
        for u,v,cost in times:
            graph[u].append((v,cost))
        
        
        heap = [(0,k)]
        
        while heap:
            time,node = heappop(heap)
            
            if ans[node] != inf: continue
            ans[node] = time
            
            for adj,cost in graph[node]:
                if time+cost<ans[adj]:
                    heappush(heap,(time+cost,adj))
                    
        ans = max(ans[1:])
        
        
        return ans if ans!=inf else -1
    
        
        
        
        