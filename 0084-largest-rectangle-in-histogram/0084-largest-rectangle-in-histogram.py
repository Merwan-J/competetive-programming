class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#         what do we want to do??
#             find the max area
        
#         brute force: considering each bar as a start point, we can search for the max area 
        
        
#         what do we know so far:
#             - its the min that matters
#             - we want as much width as possible 
        
        # ***its the min that matters ***
                # WHAT IF WE CONSIDER EACH BAR AS A MINIMUM AND SEE HOW FAR WE CAN PUSH OUR WIDTH
            
            
        ans = 0
        stack = [-1]
        n = len(heights)
        
        for i in range(n+1):
            while stack[-1]!=-1 and (i == n or heights[i]<heights[stack[-1]]):
                ans = max(ans,heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        
        return ans
        