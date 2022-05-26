class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshcount = 0
        time = 0
        rotten = collections.deque([])
        fresh = []
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    freshcount += 1
                    fresh.append((row,col))
                elif grid[row][col] == 2:
                    rotten.append((row,col))

        while rotten:
            temp = []
            
            while rotten:
                r,c = rotten.popleft()
                
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (r+i,c+j) in fresh and grid[r+i][c+j]==1:
                        grid[r+i][c+j] = 2
                        temp.append((r+i,c+j))
                        
            if temp:
                time += 1
                freshcount -= len(temp)
                rotten = collections.deque(temp)
            
        
        if freshcount>0:
            return -1
        
        return time
                
                
            
        
        
                    
        
    
        
       
            