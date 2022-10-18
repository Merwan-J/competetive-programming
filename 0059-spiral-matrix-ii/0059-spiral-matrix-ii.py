class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows,cols = n,n
        
        Border = [0,rows-1,0,cols-1]
        grid = [[0]*cols for _ in range(rows)]
        
        
        directionTurn = {
            "R":"D",
            "D":"L",
            "L":"U",
            "U":"R"
        }
        directions = {'U': [-1, 0],
                      'R': [0, 1],
                      'D': [1, 0],
                      'L': [0, -1]
                     }
        top,bottom,left,right = 0,rows-1,0,cols-1
        target = n*n
        curNum = 1
        r,c = 0,0
        curDirection = "R"


        while curNum<=target:
            grid[r][c] = curNum
            curNum+=1
            
            if curDirection == "R" and c == right:
                top+=1
                curDirection = directionTurn[curDirection]
            elif curDirection == "L" and c == left:
                bottom-=1
                curDirection = directionTurn[curDirection]
            elif curDirection == "U" and r == top:
                left+=1
                curDirection = directionTurn[curDirection]
            elif curDirection == "D" and r == bottom:
                right-=1
                curDirection = directionTurn[curDirection]
            
            dx,dy = directions[curDirection]
            r+=dx
            c+=dy
        
        return grid
                
        
    