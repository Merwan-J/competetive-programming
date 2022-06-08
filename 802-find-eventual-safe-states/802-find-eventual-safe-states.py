class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         state: 0 means good to process 1: means is being processes in the mean time

        state = [0]*len(graph)  
        memo = {}
        
        def dfs(i):
            if state[i]==1:
                return False
            
            if i in memo:
                return memo[i]
            
            state[i] = 1
            ans = True
            
            for adj in graph[i]:
                ans = ans and dfs(adj)
            
            memo[i] = ans
            state[i] = 0
            
            return memo[i]
        
        safes = []
        for i in range(len(graph)):
            if dfs(i):
                safes.append(i)
        
        return safes