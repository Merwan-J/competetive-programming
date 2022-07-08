class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        
        l = 0
        while l<len(s):
            if s[l]=="0":
                l+=1
                continue
                
            r = l + 1
            while r<len(s) and s[l]=="1"==s[r]:
                r+=1
              
            n = r-l
            ans += n*(n+1)//2
            l = r
        
        return ans%(10**9+7)