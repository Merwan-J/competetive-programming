class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                if stack[-1][1] == k -1:
                    while stack and stack[-1][0] == char:
                        stack.pop()
                else:
                    stack.append((char,stack[-1][1] + 1))
            else:
                stack.append((char,1))
        
        return "".join([char for char,count in stack])
            
                