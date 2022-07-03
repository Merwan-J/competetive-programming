class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [2,2,2,0,1,2,2,2,2]
        # [10, 1, 10, 10, 10]
        #  0   1   2   3   4
        
        l,r = 0,len(nums)-1
        
        while l<=r and nums[l]==nums[r]:
            r-=1
        
        ans = l
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid]<nums[0]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                

        return nums[ans]
        