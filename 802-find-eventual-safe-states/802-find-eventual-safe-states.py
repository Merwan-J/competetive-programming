class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         state: 0 means good to process 1: means is being processes currently, helps detect cycle

#         state = [0]*len(graph)  
#         memo = {}
        
#         def dfs(i):
#             if state[i]==1:
#                 return False
            
#             if i in memo:
#                 return memo[i]
            
#             state[i] = 1
#             ans = True
            
#             for adj in graph[i]:
#                 ans = ans and dfs(adj)
            
#             memo[i] = ans
#             state[i] = 0
            
#             return memo[i]
        
#         safes = []
#         for i in range(len(graph)):
#             if dfs(i):
#                 safes.append(i)
        
#         return safes


        incoming = [set() for _ in range(len(graph))]
        outgoing = [set(adj) for adj in graph]
        safe = [False]*len(graph)
        terminals = []
        
        for i,adj in enumerate(outgoing):
            if not adj:
                terminals.append(i)
            for node in adj:
                incoming[node].add(i)
        
        while terminals:
            node = terminals.pop()
            safe[node] = True

            for adj in incoming[node]:
                outgoing[adj].remove(node)
                if len(outgoing[adj])==0:
                    terminals.append(adj)
        
        return [i for i,isSafe in enumerate(safe) if isSafe]
    
    