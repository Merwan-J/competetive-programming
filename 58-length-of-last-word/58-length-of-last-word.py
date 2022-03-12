class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = []
        
        i = 0
        
        while i<len(s):
            temp = ""
            while i<len(s) and s[i].isalpha():
                temp+=s[i]
                i+=1
            if temp != "":
                ans.append(temp)
            i+=1
        return len(ans[-1])