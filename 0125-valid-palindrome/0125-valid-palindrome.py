class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
        
        l,r = 0,len(stack)-1
        
        while l<=r:
            if stack[l]!=stack[r]:
                return False
            l+=1
            r-=1
        
        return True