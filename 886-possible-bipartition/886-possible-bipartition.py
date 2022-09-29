class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        
        for u,v in dislikes:
            graph[u]+=[v]
            graph[v]+=[u]
        
        color = [-1]*(n+1)
        
        def check(node):
            if color[node] == -1:
                color[node] = 1
            
            for adj in graph[node]:
                if color[adj] == -1:
                    color[adj] = 1-color[node]
                    if check(adj) is False:
                        return False
                elif color[adj] == color[node]:
                    return False
            return True
                    
        
        
        for node in graph:
            if color[node] == -1 and check(node) is False:
                return False
        
        return True
                
                
        