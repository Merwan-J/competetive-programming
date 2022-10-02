class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def check(index):
            if index == len(s):
                return 1
            
            if s[index]== '0':
                return 0
            
            if index in memo:
                return memo[index]
            
            ans = check(index+1)
    
            num = int(s[index:index+2])
            if num<=26 and num>=10:
                ans += check(index+2)
            
            memo[index] = ans
            
            return memo[index]
        
        return check(0)