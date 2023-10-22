class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0]*n
        rightMin = [inf]*n
        
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],nums[i-1])
        
        for i in range(n-2,-1,-1):
            rightMin[i] = min(rightMin[i+1],nums[i+1])
        
        score = 0
        
        for i in range(1,n-1):
            if leftMax[i]<nums[i]<rightMin[i]:
                score+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                score+=1
        
        return score
            