class Solution:
    def largestRectangleArea(self, heights):
#to check the area formed by the remaining elts of the stack
        heights.append(0)
        stack = []
        maxArea = 0      
        
        for i in range(len(heights)):
            tempIndex = i
            while stack and heights[i] < stack[-1][1]:
                tempIndex = stack[-1][0]
                h = stack[-1][1]
                w = i - stack.pop()[0]
                maxArea = max(maxArea,h*w)
                
            stack.append((tempIndex,heights[i]))
        
        return maxArea
            