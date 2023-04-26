class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>9:
            total = 0
            while num:
                total+=num%10
                num = num//10 
            
            num = total
        
        
        return num 