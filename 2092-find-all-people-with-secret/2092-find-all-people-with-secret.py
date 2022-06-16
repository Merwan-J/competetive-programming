class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph =  collections.defaultdict(list)
        graph[0].append((0,firstPerson))
        
        for edge in meetings:
            u,v,time = edge
            graph[u].append((time,v))
            graph[v].append((time,u))
            
        heared = {0:0}
        q = graph[0]
        heapq.heapify(q)
        
        while q:
            time,node = heapq.heappop(q)
            if node in heared:
                continue
                
            heared[node] = time
            for t,u in graph[node]:
                if t>=time:
                    heapq.heappush(q,(t,u))
                    
        return [key for key,val in heared.items()]