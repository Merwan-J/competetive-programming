class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        nums = m*n
        
        def getCount(rows,col,target):
            count = 0
            for row in range(1,rows+1):
                count+= min(col,target//row)
            return count
        
        
        
        
        ans = 0
        l,r = 1,nums
        
        while l<=r:
            mid = l + (r-l)//2
            count = getCount(m,n,mid)
            
            if count >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
        
        
        
        