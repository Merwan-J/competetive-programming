class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        
        for char in s:
            if char == "c" and len(stack)>1 and stack[-1] == "b" and stack[-2] == "a":
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
        
        return stack == []