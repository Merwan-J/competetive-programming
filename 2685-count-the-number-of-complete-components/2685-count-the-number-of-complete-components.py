class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        def dfs(node,parent):
            self.nodes+=1
            self.path.append(node)
            
            visited.add(node)
            
            for friend in graph[node]:
                if friend == parent:
                    continue 
                if friend not in visited:
                    dfs(friend,node)
        
        count=0
        visited = set()
        
        for node in range(n):
            self.nodes = 0
            self.path = [] 
            isComplete = True
            
            if node not in visited:
                dfs(node,-1)
                
                for u in self.path:
                    if len(graph[u]) != self.nodes-1:
                        isComplete = False
                        
                if isComplete:
                    count+=1
                
        
        return count 
                