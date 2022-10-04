class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1]*n
        
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def unite(u,v):
            a = find(u)
            b = find(v)
            
            if a!=b:
                if size[a]<size[b]:
                    a,b = b,a
                parent[b] = a
                size[a]+=size[b]
        
        for u,v in edges:
            unite(u,v)
        
        
        totalNodes = 0
        ans = 0
        for node in set([find(i) for i in range(n)]):
            ans+=totalNodes*size[node]
            totalNodes += size[node]
        return ans
        
        
        
            
        
        
#         graph = [[] for _ in range(n)]
#         for u,v in edges:
#             graph[u]+=[v]
#             graph[v]+=[u]
            
#         def dfs(node):
#             if node in visited:
#                 return 0
#             visited.add(node)
#             ans = 1
#             for adj in graph[node]:
#                 if adj not in visited:
#                     ans += dfs(adj)
            
#             return ans
        
#         nodesSoFar = 0
#         unreachable = 0
#         visited = set()
        
#         for node in range(n):
#             if node not in visited:
#                 curGroupMembers = dfs(node)
#                 unreachable += nodesSoFar*curGroupMembers
#                 nodesSoFar += curGroupMembers
        
#         return unreachable