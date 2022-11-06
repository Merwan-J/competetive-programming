class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(num):
            while num%10 == 0 and num!=0:
                num//=10
            res = 0
            while num:
                lastdigit = num%10
                res = res*10 +lastdigit
                num//=10
            return res
        
        count = 0
        lookup = defaultdict(int)
        mod = 10**9 + 7
        
        for i,num in enumerate(nums):
            target = num-reverse(num)
            count+=lookup[target]
            lookup[target]+=1
        
        return count%mod
            
        
        