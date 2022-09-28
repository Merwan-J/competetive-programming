class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row,col = len(dungeon),len(dungeon[0])
        
        @cache
        def dfs(r,c):
            if r == row or c == col:
                return inf
            if r == row-1 and c == col - 1:
                return abs(dungeon[r][c])+1 if dungeon[r][c]<0 else 1
            goDown = dfs(r+1,c)
            goRight = dfs(r,c+1)
            return max(min(goDown,goRight) - dungeon[r][c],1)
        return dfs(0,0)