class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV': 4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
            
        }
        
        
        l,r = 0,1
        ans = 0
        
        while l<len(s):
            if r<(len(s)) and s[l]+s[r] in vals:
                ans += vals[s[l]+s[r]]
                l+=1
            else:
                ans+=vals[s[l]]
            l+=1
            r = l+1
            
        
        return ans
            
        
        
        