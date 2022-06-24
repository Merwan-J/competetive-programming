class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp  = [[False]*n for i in range(n)]
        
        
        for i in range(n):
            dp[i][i] = True
        
        
        lstart,lend = 0,0
        for start in range(n-1,-1,-1):
            for end in range(start+1,n):
                if s[start] == s[end] and (end-start == 1 or dp[start+1][end-1]):
                    dp[start][end] = True
                    if end-start > lend-lstart:
                        lstart = start
                        lend = end
        
        return s[lstart:lend+1]