class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(eval(b+char+a))))
            else:
                stack.append(char)
        
        return int(stack[0])
                