class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dirs=[(-1,0),(0,-1),(0,1),(1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        q=deque([])
        visit=set()

        if grid[0][0]==0:
            q.append((1,grid[0][0],0,0))
        else:
            return -1

        while q:
            path,move,i,j=q.popleft()
            if (i,j)==(n-1,n-1):
                return path

            visit.add((i,j))

            for x,y in dirs:
                dx,dy=i+x,j+y
                if 0<=dx<n and 0<=dy<n and grid[dx][dy]==0 and (dx,dy) not in visit:
                    q.append((path+1,grid[dx][dy],dx,dy))
                    visit.add((dx,dy))
        return -1
