class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_len = 0
        s  = s.split(" ")
        
        for word in s:
            max_len = max(max_len,len(word))
            
        for i in range(len(s)):
            if len(s[i])!=max_len:
                s[i]+=" "*(max_len-len(s[i]))
        
        ans = []
        
        for i in range(max_len):
            temp = []
            for word in s:
                temp.append(word[i])
            while temp[-1] == " ":
                temp.pop()
            ans.append("".join(temp))
        
        return ans
        