class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        d = 0
        i,j = 0,0
        n,m = len(nums1),len(nums2)
        
        while i<n and j<m:
            if nums1[i]>nums2[j]:
                i+=1
            else:
                d = max(d,j-i)
                j+=1
        
        return d