class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        indegree = [0]*n
        
        
        for v,u in prereq:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque()
        
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for adj in graph[node]:
                indegree[adj]-=1
                if indegree[adj] == 0:
                    q.append(adj)
        
        return sum(indegree) == 0
        