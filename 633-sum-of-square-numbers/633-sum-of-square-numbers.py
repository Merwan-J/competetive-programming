class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = {0:1}
        
        for i in range(int(math.sqrt(c))+1):
            nums[i*i] = 1
            if c-i*i in nums:
                return True
            
        return False