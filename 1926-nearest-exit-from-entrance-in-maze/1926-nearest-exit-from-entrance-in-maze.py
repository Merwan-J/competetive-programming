class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row,col = len(maze),len(maze[0])
        levels = 0
        q = deque([(entrance[0],entrance[1])])
        
        while q:
            n = len(q)
            for _ in range(n):
                r,c = q.popleft()
                if [r,c] != entrance and (r==0 or r == row-1 or c == 0 or c == col-1):
                    return levels
                
                for dr,dc in [(0,1),(-1,0),(0,-1),(1,0)]:
                    nr,nc = r+dr,c+dc
                    if -1<nr<row and -1<nc<col and maze[nr][nc] == ".":
                        maze[nr][nc] = "+"
                        q.append((nr,nc))
            levels+=1
        
        return -1
        