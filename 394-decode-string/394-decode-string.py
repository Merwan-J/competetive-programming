class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ""
                n = ""
                
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                    
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                stack.append(int(n)*temp)
            
        return "".join(stack)
        
    