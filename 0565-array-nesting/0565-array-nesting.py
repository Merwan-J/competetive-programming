class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n  = len(nums)
        
        graph = [[] for _ in range(n)]
        
        
        for node,adj in enumerate(nums):
            graph[node].append(adj)
        
        
        def dfs(node):
            visited.add(node)
            
            ans = 1
            for adj in graph[node]:
                if adj not in visited:
                    ans += dfs(adj)
            
            return ans
        
        ans = 0
        visited = set()
        
        for node in range(n):
            if node not in visited:
                ans = max(ans,dfs(node))
        
        return ans