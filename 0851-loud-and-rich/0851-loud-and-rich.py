class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        
        graph = [[] for _ in range(n)]
        
        for u,v in richer:
            graph[v].append(u)
        
        
        memo = {}
        def dfs(node,quiet):
            if node in memo:
                return memo[node]
            ans = node
            
            for adj in graph[node]:
                call = dfs(adj,quiet)
                ans = call if quiet[call]<quiet[ans] else ans
            memo[node] = ans
            return ans
        
        ans = []
        
        for node in range(n):
            ans.append(dfs(node,quiet))
        
        return ans