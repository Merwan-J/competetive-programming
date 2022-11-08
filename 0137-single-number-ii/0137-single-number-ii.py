class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        mask = 1
        
        for i in range(32):
            count = 0
            for num in nums:
                count+=num&mask
            if count%3:
                if i == 31:
                    res-=2**31
                else:
                    res+=2**i
            
            mask<<=1
        
        return res