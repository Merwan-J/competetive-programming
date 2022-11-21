class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        
        def getPowerValue(num):
            if num == 1:
                return 0
            
            if num in memo:
                return memo[num]
            
            ans = 0
            
            if num%2 == 0:
                ans = 1 + getPowerValue(num//2)
            else:
                ans = 1 + getPowerValue(num*3 + 1)
            
            memo[num] = ans
            
            return ans
        
        arr = sorted([(getPowerValue(num),num) for num in range(lo,hi+1)])
        return arr[k-1][1]