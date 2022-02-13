class Solution:
    def addDigits(self, num: int) -> int:
        def helper(num):
            if len(num)==1:
                return int(num)
            
            num = sum([int(i) for i in num])
            
            return helper(str(num))
        return helper(str(num))