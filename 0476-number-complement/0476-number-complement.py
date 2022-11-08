class Solution:
    def findComplement(self, num: int) -> int:
        n = floor(log(num,2))
        
        for i in range(n+1):
            mask = 1<<i
            num^=mask
        
        return num