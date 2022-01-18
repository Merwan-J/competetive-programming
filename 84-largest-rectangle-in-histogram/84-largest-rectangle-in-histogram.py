class Solution:
    def largestRectangleArea(self, heights):
#to check the area formed by the remaining elts of the stack
        heights.append(0)
        stack = []
        maxArea = 0      
        
        for i, height in enumerate(heights):
            startIndex = i
            while stack and heights[i] < stack[-1][1]:
                startIndex = stack[-1][0]
                index, h = stack.pop()
                w = i - index
                maxArea = max(maxArea,h*w)
                
            stack.append((startIndex,height))
        
        return maxArea
            