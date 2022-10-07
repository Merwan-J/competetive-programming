class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        ans = [[inf]*col for r in range(row)]
        
        
        q = deque([])
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    print(r,c)
                    ans[r][c] = 0
                    q.append((r,c,0))
        
        def isValid(r,c):
            return not (r<0 or r == row or c<0 or c == col or ans[r][c] != inf)
        
        while q:
            r,c,d = q.popleft()
            
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if isValid(nr,nc):
                    ans[nr][nc] = d+1
                    q.append((nr,nc,d+1))
        
        
        return ans