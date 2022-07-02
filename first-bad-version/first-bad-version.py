# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1: return 1
        l,r = 1,n
        ans = 1
        while l<r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
            
        
        if isBadVersion(r): return r
        return ans