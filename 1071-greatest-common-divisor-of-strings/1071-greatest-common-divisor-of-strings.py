class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t = ""
        
        n = min(len(str1),len(str2))
        l1,l2 = len(str1),len(str2)
        i = 0
        
        ans = ""
        while i<n:
            if str1[i] == str2[i]:
                t+=str1[i]
                i+=1
                a = len(t)
                if t*(l1//a) == str1 and t*(l2//a) == str2:
                    ans = t
            else: break
        
        return ans
       