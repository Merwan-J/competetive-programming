class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med  = int(statistics.median(nums))
        
        count = 0
        
        for num in nums:
            count += abs(num-med)
        
        return count