class Solution:
    def knightProbability(self, n: int, k: int, x: int, y: int) -> float:
        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        def isValid(r,c):
            return not(r<0 or r>=n or c<0 or c>=n)
        
        self.count = 0
        @cache
        def dfs(r,c,k):
            if k == 0:
                return 1 if isValid(r,c) else 0
            if not isValid(r,c):
                return 0
            ans = 0
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                # if isValid(nr,nc) and k>0:
                #     self.count+=1
                ans += dfs(nr,nc,k-1)

            return ans
        
        good = dfs(x,y,k)
        # print(good,self.count,good/8**k)
        return (good/8**k)