class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def findTheWinner(l,r,turn):
            if l>r:
                return 0
            
            sign = 1 if turn else -1
            
            left = sign * nums[l]  + findTheWinner(l+1,r,not turn)
            right = sign * nums[r] + findTheWinner(l,r-1,not turn)
            
            if turn:
                return max(left,right)
            return min(left,right)
        
        
        return findTheWinner(0,len(nums)-1,True)>=0