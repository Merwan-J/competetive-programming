class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
        """
        
        l,r = 0, 1
        
        while l<r and r<len(nums):
            if nums[l]==0:
                if nums[r]!=0:
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
            else:
                l+=1
            r+=1