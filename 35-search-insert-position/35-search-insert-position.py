class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def helper(start,end):
            if nums[start]==target:
                return start
            if end==start:
                return start+1 if target>nums[start] else start
            
            n = (end-start+1)//2
            
            return helper(start+n,end) if target>nums[start+n] else helper(start,end-n)
            
                
        return helper(0,n-1)