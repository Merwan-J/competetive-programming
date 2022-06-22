class Solution:
    def simplifyPath(self, path: str) -> str:
#         we dont want ..., we dont want // 
#         we dont care if it is _ we just append it to the stack
        path = path.split("/")
        stack = []
        donts = set(['/','.','..',''])
        
        for char in path:
            if stack and char == '..':
                stack.pop()
            
            if char not in donts:
                stack.append(char)
            
        return '/'+'/'.join(stack)