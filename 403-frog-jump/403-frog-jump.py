class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1:
            return False
        
        @cache
        def dp(i,last):
            if i == len(stones)-1:
                return True
            
            ans = False
            
            for jump in [last,last+1,last-1]:
                if jump == 0:
                    continue
                target = jump + stones[i]
                
                l,r = i+1,len(stones)-1
                
                while l<=r:
                    mid = l + (r-l)//2
                    
                    if stones[mid] == target:
                        ans = ans or dp(mid,jump)
                        break
                    
                    if stones[mid]>target:
                        r = mid - 1
                    else:
                        l = mid + 1
            
            return ans
        
        return dp(1,1)
        
                
                    
            