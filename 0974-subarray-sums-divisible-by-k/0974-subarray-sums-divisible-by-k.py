class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        psum = 0
        lookup = defaultdict(int)
        lookup[0]+=1
        
        for num in nums:
            psum+=num
            target = psum%k
            if target in lookup:
                ans+=lookup[target]
            lookup[target]+=1
        
        return ans