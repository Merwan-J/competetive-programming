class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,10**5
        asn = -1
        
        while l<=r:
            mid = l + (r-l)//2
            sum = mid*(mid+1)//2
            if sum == n:
                return mid
            elif sum>n:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        
        return ans
