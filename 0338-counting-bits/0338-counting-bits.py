class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(num):
            ans = 0
            
            while num:
                ans += 1&num
                num>>=1
            
            return ans
        
        res = []
        for num in range(n+1):
            res.append(count(num))
        
        return res
    
    