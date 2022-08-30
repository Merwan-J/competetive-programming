class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeros = set()
        for x,y in mines:
            zeros.add((x,y))
            
        dp = []
        for row in range(n):
            temp = []
            for col in range(n):
                temp.append([0,0,0,0])
            dp.append(temp)
        
        
#         [up,down,left,right]
#         populate the right and upward directions

        for row in range(n):
            for col in range(n-1,-1,-1):
                if (row,col) in zeros:
                    continue
                dp[row][col][3]+=1
                dp[row][col][0]+=1
                if col + 1<n:
                    dp[row][col][3]+=dp[row][col+1][3]
                if row -1>-1:
                    dp[row][col][0]+=dp[row-1][col][0]
                    
        for row in range(n-1,-1,-1):
            for col in range(n):
                if (row,col) in zeros:
                    continue
                dp[row][col][2]+=1
                dp[row][col][1]+=1
                if col - 1>-1:
                    dp[row][col][2]+=dp[row][col-1][2]
                if row +1<n:
                    dp[row][col][1]+=dp[row+1][col][1]
        
        ans = 0
        for row in range(n):
            for col in range(n):
                ans = max(ans,min(dp[row][col]))
        
        return ans
        
        
        
    