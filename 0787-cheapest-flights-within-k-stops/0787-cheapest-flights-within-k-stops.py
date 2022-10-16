class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = [[] for _ in range(n)]
        
        for u,v,w in flights:
            graph[u].append((v,w))
        
        q = [(0,src,k)]
        visited = defaultdict(int)
        
        while q:
            cost,node,stops = heappop(q)
            if node == dst:
                return cost
            
            if stops<0 or (node in visited and visited[node]>=stops):
                continue

            visited[node] = stops
                            
            for adj,w in graph[node]:
                heappush(q,(cost+w,adj,stops-1))
        
        return -1
            