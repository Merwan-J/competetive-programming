class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        left_min = [inf]*n
        
        
        for i in range(1,n):
            left_min[i] = min(left_min[i-1],nums[i-1])
        
        
        stack = []
        
        for i in range(n-1,-1,-1):
            if nums[i]<=left_min[i]:
                continue
            
            while stack and stack[-1]<=left_min[i]:
                stack.pop()
            
            if stack and stack[-1]<nums[i]:
                return True
            
            stack.append(nums[i])
        
        return False