class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        
        for li in grid:
            l,r = 0,len(li)-1
            pos = len(li)
            
            while l<=r:
                mid = (l+r)//2
                
                if li[mid]<0:
                    pos = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            total += len(li)-pos
        
        return total