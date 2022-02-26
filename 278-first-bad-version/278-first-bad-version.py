# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        mid = start + (end-start)//2
       
        while start<=end:
            if start==end:
                if isBadVersion(start):
                    return start
                return start+1
            if isBadVersion(mid):
                end = mid-1
            else:
                start = mid+1
            mid = start + (end-start)//2
        
        return start