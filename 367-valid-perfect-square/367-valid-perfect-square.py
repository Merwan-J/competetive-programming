class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num
        
        def helper(l,r):
            mid = (l+r)//2
            if l>r:
                return False
            if mid*mid == num:
                return True
            
            if mid**2 > num:
                return helper(l,mid-1)
            return helper(mid+1,r)
        
        return helper(l,r)
            
            