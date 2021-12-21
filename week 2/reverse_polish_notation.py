class Solution:
    
    
    def calculate(self,left,right,i):
        if i == '+':
            total = left + right
        elif i == '*':
            total = left * right
        elif i == '-':
            total = left - right
        else:
            total = int(left / right)
        print(left,right,i,"calculated")
        return total

    def evalRPN(self, li: List[str]) -> int:
        d = '/*-+'
        stack = []
        for i in li:
            if i in d:
                total = self.calculate(stack[-2],stack[-1],i)
                stack = stack[:-2]
                stack.append(total)
            else:
                stack.append(int(i))
        return stack[0]
        
