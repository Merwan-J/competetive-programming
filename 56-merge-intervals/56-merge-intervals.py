class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda item: item[0])
        stack = [intervals[0]]
        
        for i in range(1,len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                if stack[-1][1]>=intervals[i][1]:
                    pass
                else:
                    stack[-1][1] = intervals[i][1]
            else:
                stack.append(intervals[i])
                
        return stack            
        
                        
        