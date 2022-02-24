class Solution:
    def removeKdigits(self, li: str, k: int) -> str:
        stack = []
        
        for i in li:
            while stack and k>0 and int(i)<int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(i)
            
        while stack and k>0:
            stack.pop()
            k-=1
        
        stack = "0" if stack==[] else stack
        
        ans = "".join(stack)
        
        
        return str(int(ans))
    
   

        
