class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dp(i,j,turn):
            if i>j:
                return 0
            if(i,j) in memo:
                return memo[(i,j)]
            if turn == 1:
                a = nums[i] + dp(i+1,j,-1)
                b = nums[j] + dp(i,j-1,-1)
                memo[(i,j)] = max(a,b)
            else:
                a = -nums[i] + dp(i+1,j,1)
                b = -nums[j] + dp(i,j-1,1)
                memo[(i,j)] = min(a,b)
                
            return memo[(i,j)]
        
        return dp(0,len(nums)-1,1)>=0