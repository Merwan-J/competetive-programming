class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet) 
        graph = [[] for _ in range(n)]
        indegree = [0]*n
        ans = [i for i in range(n)]
        
        for u,v in richer:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque([])
        for node,val in enumerate(indegree):
            if val == 0:
                q.append(node)
            
        while q:
            node = q.popleft()
            for adj in graph[node]:
                indegree[adj]-=1
                if quiet[ans[node]]<quiet[ans[adj]]:
                    ans[adj] = ans[node]
                if indegree[adj] == 0:
                    q.append(adj)        
        
        return ans
        
        