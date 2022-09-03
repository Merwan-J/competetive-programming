class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def dfs(total):
            if total == 0:
                return 1
            ans = 0
            for num in nums:
                if total-num>=0:
                    ans+= dfs(total-num)
            return ans
        
        return dfs(target)
        
            
            