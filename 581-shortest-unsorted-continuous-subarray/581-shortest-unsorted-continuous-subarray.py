class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)

        ans = []
        
        for i in range(len(nums)):
            if nums[i]!=s[i]:
                ans.append(i)
        return 0 if not ans else ans[-1]-ans[0] + 1
        