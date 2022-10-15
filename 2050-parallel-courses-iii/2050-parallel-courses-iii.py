class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prevTime = [0]*n
        graph = [[] for _ in range(n)]
        indegree = [0]*n
        
        for u,v in relations:
            graph[u-1].append(v-1)
            indegree[v-1]+=1
            
        q = deque([node for node in range(n) if indegree[node] == 0])
        
        while q:
            node = q.popleft()
            prevTime[node]+=time[node]
            
            for adj in graph[node]:
                prevTime[adj] = max(prevTime[adj],prevTime[node])
                indegree[adj]-=1
                if indegree[adj] == 0:
                    q.append(adj)
        
        return max(prevTime)
                