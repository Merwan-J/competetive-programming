class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        pos = 0 
        
        while l<=r:
            mid = (l+r)//2
            
            if (nums[mid] >= nums[0] and nums[mid]>=nums[-1]):
                l = mid + 1
            elif (nums[mid] <= nums[0] and nums[mid]<=nums[-1]):
                pos = mid
                r = mid - 1
            else:
                break
                
        l,r = 0,len(nums)-1
        
        if pos != 0:
            if target == nums[l]:
                return l
            if target > nums[l]:
                r = pos - 1
            else:
                l = pos 
                
        while l<=r:
            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
            