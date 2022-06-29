class Solution:
    def findGCD(self, nums: List[int]) -> int:
        large = max(nums)
        small = min(nums)
        ans = 1
        
        for i in range(1,small+1):
            if small%i == large%i == 0:
                ans = i
        
        return ans