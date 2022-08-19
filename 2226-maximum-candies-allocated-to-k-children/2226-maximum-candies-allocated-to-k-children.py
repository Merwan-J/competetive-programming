class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid,k):
            count = 0
            for candy in candies:
                count+=candy//mid
            
            return count>=k
        
        
        l,r = 1,max(candies)
        ans = 0
        
        while l<=r:
            mid = l + (r-l)//2
            
            if check(mid,k):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans