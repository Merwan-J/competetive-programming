class Solution:
    def isValid(li):
        pairs = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = []
        for i in li:
            if i in pairs:
                stack.append(i)
            else:
                if len(stack) != 0 and i == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True
        
