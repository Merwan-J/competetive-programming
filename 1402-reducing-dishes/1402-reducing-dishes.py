class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def dp(i,time):
            if i == len(satisfaction):
                return 0
            
            include = time*satisfaction[i] + dp(i+1,time+1)
            notinclude = dp(i+1,time)
            
            return max(include,notinclude)
        
        return dp(0,1)