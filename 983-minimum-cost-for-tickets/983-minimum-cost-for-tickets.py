class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(i):
            if i == len(days):
                return 0
            
            ans = float('inf')
            
            for day,cost in zip([1,7,30],costs):
                j = i
                while j<len(days) and days[j] < days[i]+day:
                    j+=1
                
                ans = min(ans,dp(j)+cost)
                
            return ans
        
        return dp(0)
                    

                    
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        