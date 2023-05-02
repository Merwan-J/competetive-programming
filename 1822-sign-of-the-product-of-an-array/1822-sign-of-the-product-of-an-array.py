class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signFunc = lambda x: 0 if x == 0 else x//abs(x) 
        ans = 1 
        
        for num in nums:
            ans*=num
        
        return signFunc(ans)
        
        