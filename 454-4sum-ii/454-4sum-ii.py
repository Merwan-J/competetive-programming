class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        hashMap = collections.defaultdict(int)
        ans = 0
        
        for i in range(n):
            for j in range(n):
                hashMap[nums1[i] + nums2[j]]+=1
        
        for k in range(n):
            for l in range(n):
                ans += hashMap[0-(nums3[k]+nums4[l])]
        
        return ans
        
                        
        