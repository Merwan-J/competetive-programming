class Solution:
    def isValid(self,s):
        valids = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        
        stack = []
        
        for i in s:
            if not stack and i not in valids:
                return False
            if i in valids:
                stack.append(i)
            else:
                if i==valids[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack==[]
            