class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(n):
            if n == 1:
                return "1"
            
            prevSay = helper(n-1)
            stack = []
                        
            for num in prevSay:
                if stack and stack[-1][0] == num:
                    stack[-1] = (num,stack[-1][1]+1)
                else:
                    stack.append((num,1))
                    
            for i,tup in enumerate(stack):
                num,count = tup 
                stack[i] = str(count) + num 
            
                
            
            return "".join(stack)
        
        
        return helper(n)
    