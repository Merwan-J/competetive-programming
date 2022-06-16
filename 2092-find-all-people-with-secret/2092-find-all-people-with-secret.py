class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self,child):
        if self.parents[child]==child:
            return child
        parent = self.find(self.parents[child])
        return parent
    def union(self,child,parent):
        self.parents[self.parents[child]] = self.find(parent)
        
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # uf = UF(n)
        graph =  collections.defaultdict(list)
        graph[0].append((0,firstPerson))
        for edge in meetings:
            u,v,time = edge
            graph[u].append((time,v))
            graph[v].append((time,u))
            
        # for vertex,edges in graph.items():
        #     graph[vertex] = sorted(edges)
        
        # def dfs(node,target):
        #     pass
        
        heared = {0:0}
        q = graph[0]
        heapq.heapify(q)
        # print(q)
        while q:
            time,node = heapq.heappop(q)
            if node in heared:
                continue
            heared[node] = time
            for t,u in graph[node]:
                if t>=time:
                    heapq.heappush(q,(t,u))
        # print(heared)
        return [key for key,val in heared.items()]