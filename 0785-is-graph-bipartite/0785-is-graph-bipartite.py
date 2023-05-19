class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        
        def check(node):
            if color[node] == -1:
                color[node] = 1
            
            for adj in graph[node]:
                if color[adj]==-1:
                    color[adj] = 1-color[node]
                    if check(adj) == False:
                        return False
                elif color[adj]==color[node]:
                    return False
            return True
        
        for node in range(n):
            if color[node]==-1:
                if check(node) == False:
                    return False
        return True