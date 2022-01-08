class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        popped = popped[::-1]
        pushed = pushed[::-1]
        stack = []

        while len(pushed)!=0:
            stack.append(pushed.pop())
            if stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
                while len(stack)!=0 and stack[-1] == popped[-1]:
                    stack.pop()
                    popped.pop()
        return True if len(stack) == 0 else False
