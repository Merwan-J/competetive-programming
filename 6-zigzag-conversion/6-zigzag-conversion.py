class Solution:
    def convert(self, s: str, rows: int) -> str:
        if rows==1:
            return s
        down  = True
        chars = dict()
        count = 1
        
        for i in range(len(s)):
            if count == 1 and not down:
                down = True
            elif count == rows and down:
                down = False
            
            chars[count] = chars.get(count,"")+s[i]
            
            count = count + 1 if down else count - 1
            
        
        
        ans = ""
        
        chars = list(chars.items())
        chars.sort()
        
        for i in chars:
            ans += i[1]
        return ans