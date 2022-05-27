class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[1])
        i = 0
        count = 0
        print(intervals)
        while i<len(intervals):
            end = intervals[i][1]
            i += 1
            while i<len(intervals) and end>intervals[i][0]:
                count += 1
                
                # print(end,intervals[i][0])
                i+=1
        
        return count