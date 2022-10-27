class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @cache
        def dp(start,end):
            if start >= end:
                return 0
            ans = inf
            
            for cut in cuts:
                if cut>start and cut<end:
                    left = dp(start,cut)
                    right = dp(cut,end)
                    ans = min(ans,left+right + end-start)
            return 0 if ans == inf else ans
        
        return dp(0,n)