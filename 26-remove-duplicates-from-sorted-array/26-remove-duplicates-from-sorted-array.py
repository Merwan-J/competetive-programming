class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums==[]:
            return 0

        l,r = 0,1
        n = len(nums)-1
        
        while r<= n:
            if nums[l]==nums[r]:
                nums.pop(r)
                n-=1
                continue 
            l+=1
            r+=1
        return n+1