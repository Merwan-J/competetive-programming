class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def left(l,r):
            start = r
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    start = mid
                    r = mid-1
                else:
                    l = mid + 1
            return start
        
        def right(l,r):
            end = l
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    end = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return end
        
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid]==target:
                start = left(l,mid)
                end = right(mid,r)
                return [start,end]
                
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        
        return [-1,-1]