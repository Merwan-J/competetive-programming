class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        def backtrack(node,path):
            if node == n-1:
                ans.append(list(path))
                return 
            
            for adj in graph[node]:
                path.append(adj)
                backtrack(adj,path)
                path.pop()
        
        
        backtrack(0,[0])
        
        return ans
                