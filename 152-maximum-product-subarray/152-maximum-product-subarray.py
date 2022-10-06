class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        the_max, the_min = nums[0] , nums[0]
        ans = the_max

        for idx in range(1, len(nums)):
            new_max = max(the_min * nums[idx], the_max * nums[idx], nums[idx])
            new_min = min(the_max * nums[idx], the_min * nums[idx], nums[idx])

            the_max, the_min = new_max, new_min
            ans = max(ans, the_max)

        return ans
    
    