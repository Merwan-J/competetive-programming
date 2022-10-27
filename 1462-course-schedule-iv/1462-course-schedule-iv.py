class Solution:
    def checkIfPrerequisite(self, n: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        connected = [[False]*n for _ in range(n)]
        
        for u,v in prereq:
            connected[u][v] = True
        
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
        
        
        return [connected[i][j] for i,j in queries]