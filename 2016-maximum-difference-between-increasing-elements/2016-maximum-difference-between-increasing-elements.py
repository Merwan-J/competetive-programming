class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        arr = [float('-inf')]*len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            arr[i] = max(nums[i+1],arr[i+1])
                
        ans = -1
        
        for i in range(len(nums)-1):
            if nums[i]<arr[i]:
                ans = max(ans,arr[i]-nums[i])
        return ans 
    
        