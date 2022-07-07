class Solution:
    def maxPower(self, s: str) -> int:
        long = 1
        i =0
        
        while i<len(s):
            cur = s[i]
            i+=1
            count = 1
            
            while i<len(s) and cur == s[i]:
                count +=1
                i+=1
            long = max(count,long)
        
        return long