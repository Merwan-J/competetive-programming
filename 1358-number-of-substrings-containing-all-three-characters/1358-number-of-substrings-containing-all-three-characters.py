class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l,r = 0,0
        count = {}
        ans = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1 
            while len(count) == 3:
                ans+= len(s)-r
                count[s[l]]-=1
                if count[s[l]] == 0:
                    del count[s[l]]
                
                l+=1
        
        return ans
            
                
                
        