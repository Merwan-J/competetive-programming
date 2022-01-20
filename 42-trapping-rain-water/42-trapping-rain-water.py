class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        total = 0
        
        maxIndex = (0,0)
        
        for i in range(len(height)):
            if height[i] > maxIndex[1]:
                maxIndex = (i,height[i])
        
        maxL=height[0]
        maxR = height[-1]
        
        for i in range(1,maxIndex[0]):
            maxL = max(maxL,height[i])
            total += maxL-height[i]
        
        for i in range(len(height)-2,maxIndex[0],-1):
            maxR = max(maxR,height[i])
            total += maxR-height[i]
        
        return total