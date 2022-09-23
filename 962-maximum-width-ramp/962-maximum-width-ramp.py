class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = sorted((num,i) for i,num in enumerate(nums))
        stack = []
        ans = 0
        for tup in arr:
            while stack and not(stack[-1][0]<=tup[0] and stack[-1][1]<=tup[1]):
                stack.pop()
            stack.append(tup)
            ans = max(ans,tup[1]-stack[0][1])
        
        return ans