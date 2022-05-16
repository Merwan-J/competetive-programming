class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def check(n):
            total = 0
            for i in nums:
                total += ceil(i/n)
            return total<= threshold
        
        
        l,r = 1,max(nums)
        
        while l<=r:
            mid = (l+r)//2

            if check(mid):
                r = mid - 1 
            else:
                l = mid + 1
        return l