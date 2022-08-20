class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        nums = sorted(list(set(nums)))
        memo = {}

        @cache
        def helper(i,deleted,):
            if i >= len(nums):
                return 0
         
            dontPick = helper(i+1,False)
            pick = counter[nums[i]]*nums[i] + helper(i+1,True) if not(deleted and nums[i-1]+1==nums[i]) else 0
            
            return max(dontPick,pick)
        
        return helper(0,False)