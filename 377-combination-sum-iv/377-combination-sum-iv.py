class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        
        def helper(target):
            if target<0:
                return 0
            
            if target == 0:
                return 1
            if target in memo:
                return memo[target]

            for num in nums:
                memo[target] += helper(target-num)
            
            return memo[target]
                
        helper(target)
        
        return memo[target]