class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for num in pushed:
            stack.append(num)
            while stack and i<len(popped) and stack[-1]==popped[i]:
                stack.pop()
                i+=1
                
        return stack==[]
    