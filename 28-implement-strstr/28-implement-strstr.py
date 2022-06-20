class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i<len(haystack):
            if haystack[i] == needle[0]:
                l = i
                k = 0
                
                temp = ""
                while l<len(haystack) and k<len(needle) and needle[k]==haystack[l]:
                    temp += haystack[l]
                    l+=1
                    k+=1
                if temp == needle:
                    return i
            i+=1
            
        return -1