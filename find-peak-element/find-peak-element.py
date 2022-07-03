class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ans = 0
        nums.append(float('-inf'))
        while l<=r:
            mid = l + (r-l)//2
            
            if mid > 0 and nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            if mid == 0 or nums[mid] >= nums[mid-1]:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
            
        