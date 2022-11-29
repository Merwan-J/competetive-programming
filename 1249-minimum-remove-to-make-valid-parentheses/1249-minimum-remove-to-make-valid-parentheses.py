class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closers_left = 0
        openers_sofar = 0
        
        
         
        for char in s:
            if char == ")":
                closers_left+=1
            
        stack = []
        
        for char in s:
            if char.isalpha():
                stack.append(char)
            elif char == "(" and closers_left>0:
                stack.append(char)
                openers_sofar+=1
                closers_left-=1
            elif char == ")":
                if openers_sofar>0:
                    stack.append(char)
                    openers_sofar-=1
                else: 
                    closers_left-=1
        
        return "".join(stack)
            
        
    
        
        
        
        
        
