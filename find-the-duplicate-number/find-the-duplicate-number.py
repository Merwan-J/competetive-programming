class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r  = 1,len(nums)-1
        ans = -1
        
        while l<=r:
            mid = (l+r)//2
            total = sum(num<=mid for num in nums)
            
            if total > mid:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans