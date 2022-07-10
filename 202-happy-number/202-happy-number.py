class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(num):
            ans = 0
            while num:
                ans += (num%10)**2
                num //= 10
            return ans
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = nextNum(n)
        
        return n == 1
    