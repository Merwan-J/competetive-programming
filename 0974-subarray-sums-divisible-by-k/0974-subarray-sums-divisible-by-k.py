class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        psum = 0
        counter = defaultdict(int)
        counter[0] = 1
        
        for num in nums:
            psum+=num
            count+=counter[psum%k]
            counter[psum%k]+=1
        
        return count
        