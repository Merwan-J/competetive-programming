class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0:-1}
        total = 0
        
        for i,num in enumerate(nums):
            total+=num
            
            if total%k in mods and i - mods[total%k] > 1:
                return True
            elif total%k not in mods:
                mods[total%k] = i
            
        return False
        