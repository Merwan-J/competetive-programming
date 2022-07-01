class Solution:
    def minAddToMakeValid(self, s: str) -> int:
#         stack = []
        
#         for c in s:
#             if stack and c==')' and stack[-1] == '(':
#                 stack.pop()
#                 continue
#             stack.append(c)
        
#         return len(stack)
        
        need_right,need_left = 0,0
        
        for c in s:
            if c == '(':
                need_right+=1
            elif c==')':
                need_right-=1
                
            if need_right == -1:
                need_left+=1
                need_right = 0
        
        return need_right+need_left