class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         arr = [0]*len(nums)
        
#         for i in range(len(nums)):
#             arr[(i+k)%len(nums)] = nums[i]
            
#         for i in range(len(nums)):
#             nums[i] = arr[i]
        
        
        def reverse(arr,left,right):
            while left<right:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
        
# incase k is greater than the length of nums, this makes it in the range of the length
        k = k % len(nums)
        
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

            
        
        

        
        
        
        
        