class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = collections.Counter(nums1)
        ans = []
        for num in nums2: 
            if num in counter and num not in ans:
                ans.append(num)
        
        return ans