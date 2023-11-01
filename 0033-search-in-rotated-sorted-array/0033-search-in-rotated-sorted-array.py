class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        if nums[ans] == target:
            return ans 
        elif nums[0]>target:
            l,r = ans + 1,n-1 
        else:
            l,r = 0, ans - 1
        
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
            
            