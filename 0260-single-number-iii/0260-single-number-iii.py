class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = 0
        for num in nums:
            ans^=num
        
        mask = 1
        for i in range(32):
            if mask&ans:
                break
            mask <<= 1
        
        num1 = 0
        num2 = 0
        
        for num in nums:
            if num&mask:
                num1^=num
            else:
                num2^=num
        
        return [num1,num2]
        
        