class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left = float('inf')
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                left = min(stack.pop(),left)
            stack.append(i)
        
        if left == float('inf'):
            return 0
        
        
        stack = []
        right = float('-inf')
        
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<nums[i]:
                right = max(stack.pop(),right)
            stack.append(i)
        
        return right - left + 1 
            
            
            