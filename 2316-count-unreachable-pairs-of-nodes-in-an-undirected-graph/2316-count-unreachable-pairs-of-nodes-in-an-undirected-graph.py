class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u]+=[v]
            graph[v]+=[u]
            
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            ans = 1
            for adj in graph[node]:
                if adj not in visited:
                    ans += dfs(adj)
            
            return ans
        
        nodesSoFar = 0
        unreachable = 0
        visited = set()
        
        for node in range(n):
            if node not in visited:
                curGroupMembers = dfs(node)
                unreachable += nodesSoFar*curGroupMembers
                nodesSoFar += curGroupMembers
        
        return unreachable