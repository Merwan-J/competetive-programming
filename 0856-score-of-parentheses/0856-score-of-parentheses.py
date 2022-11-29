class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
    
        # initalize a stack
        stack = []
        
        # traverse the string
        for char in s:
        # if encountered a ( : push it to the stack
            if char == "(":
                stack.append(char)
                             
        # if encountered ) and if the top of the stack is (
            # -pop it and replace it with 1 i.e the score of it
            elif char == ")" and stack[-1] == "(":
                stack.pop()
                stack.append(1)
                             
        # if enountered ) and the top of the stack is a number, 
            # - pop from the top of the stack until no number is at the top of the stack, then if              the stack is empty append the sum of those number else pop the elt at the top("("              opening bracket) and push the 2 * sum  to the stack
            elif char == ")" and stack[-1]!="(":
                cur = 0
                while stack and stack[-1]!="(":
                    cur+=stack.pop()
                # if stack:
                stack.pop()
                cur = 2 * cur
                stack.append(cur)
                
        return sum(stack)
    
    
    
