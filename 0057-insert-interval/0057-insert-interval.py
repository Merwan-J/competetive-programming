class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        
        for start,end in intervals:
            if ans and ans[-1][1]>=start:
                last = ans.pop()
                newEnd = max(last[1],end)
                ans.append([last[0],newEnd])
            else:
                ans.append([start,end])
        
        return ans
        
        