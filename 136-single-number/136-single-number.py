class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = collections.Counter(nums)
        
        for key,value in counter.items():
            if value == 1:
                return key
        
        