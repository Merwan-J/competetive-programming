class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.strip() == "":
            return True
        strng = ""
        
        for i in s:
            if i.isalpha():
                strng += i.lower()
            elif i.isnumeric():
                strng += i
        
        l,r = 0,len(strng)-1
        while l<r:
            if strng[l] != strng[r]:
                return False
            l+=1
            r-=1
        return True