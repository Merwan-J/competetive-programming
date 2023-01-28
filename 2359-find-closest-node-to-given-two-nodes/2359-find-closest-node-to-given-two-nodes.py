class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
        graph = [[] for _ in range(n)]
        path1 = [inf]*n 
        path2 = [inf]*n
        
        
        for i,adj in enumerate(edges):
            if adj!=-1:
                graph[i].append(adj)
        
        
        def dfs(node,dist,path):
            if node in visited:
                return 
            visited.add(node)
            path[node] = dist
            
            for adj in graph[node]:
                dfs(adj,dist+1,path)
                
        visited = set()
        dfs(node1,0,path1)
        visited = set()
        dfs(node2,0,path2)
        
        dist = inf
        ans = -1
        

        for i in range(n):
            cur = max(path1[i],path2[i])
            
            if cur<dist:
                ans = i
                dist = cur
        
        return ans 
            
        