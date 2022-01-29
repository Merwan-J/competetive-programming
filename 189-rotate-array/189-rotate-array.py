class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = [0]*len(nums)
        
        for i in range(len(nums)):
            arr[(i+k)%len(nums)] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = arr[i]
            
        
        

        
        
        
        
        