class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        obstacles = set()
        visited = set()
        for i,j in guards:
            obstacles.add((i,j))
        
        for i,j in walls:
            obstacles.add((i,j))
            
            
        def dfs(i,j,v,h):
            if not (i>-1 and i<m and j<n and j>-1) or (i,j) in obstacles:
                return 
            
            if (i,j) not in visited:
                visited.add((i,j))
            
            dfs(i+v,j+h,v,h)
        
        
        for i,j in guards:
            for a,b in [[0,1],[1,0],[-1,0],[0,-1]]:
                dfs(i+a,j+b,a,b)

        return m*n-len(visited)-len(obstacles)
        