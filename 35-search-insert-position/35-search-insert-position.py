class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        
        l,r = 0,len(nums)-1
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
