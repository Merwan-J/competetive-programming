class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda item: item[1])
#         i = 0
#         count = 0
#         print(intervals)
#         while i<len(intervals):
#             end = intervals[i][1]
#             i += 1
#             while i<len(intervals) and end>intervals[i][0]:
#                 count += 1
#                 i+=1
        
#         return count
    
    
        intervals.sort(key=lambda item: item[0])
        count = 0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd,end)
        
        return count
    
    
    
#     idea: to find the minimum deletion to create a non overlapping intervals

# intution: 

# sort the intervals by thier start value, and check wether the adjecent intervals in the sorted array are overlapping or not. 
# the check for overlapping can be done by comparing the end point of the first interval with the start point of the second interval.

# if the two intervals are overlapping, one of them has to be removed. The one that is going to be removed is the interval with smalles ending point.
# 	i.e there will be less chance that the one remaing interval will overlap with the next comming one if it ends first. 
# 		since the whole idea is to minimize deletion

# we have to also save the smallest ending point so that we can compare it to the next interval.

# we could do this question with the same concepth but different way by sorting the intervals by their ending point



