class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = popped[::-1]

        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[-1]:
                stack.pop()
                popped.pop()

        return stack==[]
    