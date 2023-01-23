class Solution:
    def minCut(self, s: str) -> int:
        
        
        memo = {}
        
        def checkPalindrome(start,end):
            if start>end:
                return True
            
            if (start,end) in memo:
                return memo[(start,end)]
            
            ans = False
            if s[start]!=s[end]:
                ans = False
            else:
                ans = checkPalindrome(start+1,end-1)
            
            memo[(start,end)] = ans
            return ans
        
        
        
        @cache
        def cut(i):
            if i == len(s):
                return -1
            
            ans = inf
            
            for j in range(i,len(s)):
                if checkPalindrome(i,j):
                    ans = min(ans,1+cut(j+1))
            
            return ans
        
        return cut(0)