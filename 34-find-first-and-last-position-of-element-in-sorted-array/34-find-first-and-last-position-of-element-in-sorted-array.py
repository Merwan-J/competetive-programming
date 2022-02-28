class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid = l + (r-l+1)//2
            
            if nums[mid]==target:
                start,end = mid,mid
                while end+1<len(nums) and nums[end+1]==target:
                    end+=1
                while start-1>-1 and nums[start-1]==target:
                    start-=1
                break
            
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            
            
        
        
        return [start,end]