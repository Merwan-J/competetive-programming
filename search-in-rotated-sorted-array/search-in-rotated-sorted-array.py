class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        pivot = 0
        
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]<nums[0]:
                pivot = mid
                r = mid - 1
            else:
                l = mid + 1
        if target > nums[-1]:
            l,r = 0,pivot-1
        else:
            l,r = pivot,len(nums)-1
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid -1
            else:
                l = mid + 1
        
        return -1