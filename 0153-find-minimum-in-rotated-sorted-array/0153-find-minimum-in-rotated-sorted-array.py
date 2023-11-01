class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = n-1
        
        while l<=r: 
            mid = l + (r-l)//2
            
            if nums[mid]>=nums[l]:
                if nums[mid]>nums[ans]:
                    ans = mid 
                l = mid + 1 
            else:
                r = mid - 1
        
        return nums[(ans+1)%n]
        
        
        