class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0]*n
        
        for u,v in edges:
            indegrees[v]+=1
        
        return [node for node in range(n) if indegrees[node] == 0]