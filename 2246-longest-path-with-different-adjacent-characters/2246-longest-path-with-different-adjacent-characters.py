class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        if n == 1:
            return 1
        
        graph  = [[] for _ in range(n)]
#         u->v
        for v,u in enumerate(parent):
            if u == -1:
                continue
            graph[u]+=[v]
        
        
        ans = 0
        def dfs(node):
            nonlocal ans
            if graph[node] == []:
                return 1
            
            maxOne = 0
            maxTwo = 0
            
            for child in graph[node]:
                curCall = dfs(child)
                if s[child]!=s[node]:
                    if curCall>maxOne:
                        maxOne,maxTwo = curCall,maxOne
                    elif curCall>maxTwo:
                        maxTwo = curCall
            
            ans = max(ans,maxOne+maxTwo+1)
            return max(maxOne,maxTwo) + 1
        
        dfs(0)
        return ans