class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        stop = set(restricted)
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            if u in stop or v in stop:
                continue
            graph[u].append(v)
            graph[v].append(u)
        
        
#         def dfs(node,prev):
#             visited.add(node)
#             for adj in graph[node]:
#                 if adj != prev and adj not in visited:
#                     dfs(adj,node)
        
#         visited = set()
#         dfs(0,-1)
        
#         return len(visited)

        ans = 0
        q = deque([(0,-1)])
        
        while q:
            n = len(q)
            ans+=n
            for _ in range(n):
                node,prev = q.popleft()
                for adj in graph[node]:
                    if adj != prev:
                        q.append((adj,node))
            
        
        return ans
        
        
        