class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        
        for node,boss in enumerate(manager):
            if boss!=-1:
                graph[boss].append(node)
        
        
        def dfs(node):
            ans = 0            
            for child in graph[node]:
                ans = max(ans,dfs(child))     
            
            return ans + informTime[node]
        
        return dfs(headID)
    
