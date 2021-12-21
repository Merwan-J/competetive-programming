class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        op = '()'
        stack = []
        output = ''

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                sub_s = s[stack[-1]+1:i][::-1]
                b_rest_s = s[:stack[-1]+1]
                t_rest_s = s[i:]
                s = b_rest_s+sub_s+t_rest_s
                stack = stack[:-1]
        for i in s:
            if i not in op:
                output+=i

        return output
