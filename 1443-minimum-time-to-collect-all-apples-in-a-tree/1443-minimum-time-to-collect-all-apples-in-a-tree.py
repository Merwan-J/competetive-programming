class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,parent):
            if node is None:
                return False
            
            flag = hasApple[node]            
            
            for adj in graph[node]:
                if adj!=parent and dfs(adj,node):
                    ans[0]+=2
                    flag = True
            
            return flag
    
        ans = [0]
        dfs(0,-1)
        
        return ans[0]
        