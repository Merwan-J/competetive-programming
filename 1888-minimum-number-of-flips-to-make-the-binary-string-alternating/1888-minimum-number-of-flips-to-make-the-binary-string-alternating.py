class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s *= 2
        alt1,alt2 = "",""
        for i in range(len(s)):
            alt1 += '1' if i%2 else '0'
            alt2 += '0' if i%2 else '1'
        
        diff1,diff2 = 0,0
        l = 0
        ans = float('inf')
        
        for r in range(len(s)):
            if s[r]!=alt1[r]:
                diff1 += 1
            if s[r]!=alt2[r]:
                diff2 += 1
            
            if (r-l+1)>n:
                if s[l]!=alt1[l]:
                    diff1 -= 1
                if s[l]!=alt2[l]:
                    diff2 -= 1
                l+=1
            
            if (r-l+1) == n:
                ans = min(ans,diff1,diff2)
        
        return ans
        
        
        
        
        