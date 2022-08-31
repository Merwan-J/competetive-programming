class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        mono_stack = []
        for ind ,num in enumerate(nums):
            while mono_stack and mono_stack[-1][0] < num:
                cur = mono_stack.pop()
                ans[cur[1]] = ind - cur[1]
            mono_stack.append((num , ind))
        return ans