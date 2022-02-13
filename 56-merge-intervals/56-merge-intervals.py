class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda item: item[0])
        stack = [intervals[0]]
        
        for i in range(1,len(intervals)):
            
            if stack[-1][1] >= intervals[i][0] and stack[-1][1]<intervals[i][1]:
                stack[-1][1] = intervals[i][1]
                
            elif stack[-1][1]<intervals[i][0]:
                stack.append(intervals[i])
                
        return stack            
        
                        
        