class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = [] 
        
        
        for char in s: 
            if char in pairs and stack and pairs[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return stack == []
                