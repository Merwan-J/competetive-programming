class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def dfs(r,c,i):
            if i == len(word)-1 and board[r][c]==word[i]:
                return True 
            
            path.add((r,c))
            ans = False 
            
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc = r+x,c+y
                
                # inbound, match go 
                if (-1<nr<len(board) and -1<nc<len(board[0]) and (nr,nc) not in path and
                    i+1<len(word) and board[nr][nc]==word[i+1]):
                    ans = ans or dfs(nr,nc,i+1)                
            path.remove((r,c))
            return ans 
        
        # visited clear it every time you get starting letter 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    path = set() 
                    if dfs(r,c,0): return True
        
        return False