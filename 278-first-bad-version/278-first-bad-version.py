# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        bad = -1
        
        l,r = 1,n
        
        while l<=r:
            mid = (l+r)//2
            
            if isBadVersion(mid):
                bad = mid
                r = mid-1
            else:
                l = mid + 1
            
        
        return bad
        