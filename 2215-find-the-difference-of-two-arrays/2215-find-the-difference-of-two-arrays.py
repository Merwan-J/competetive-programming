class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Unique = set(nums1)
        nums2Unique = set(nums2)
        
        for num in nums1:
            if num in nums2Unique:
                nums2Unique.remove(num)
        
        for num in nums2:
            if num in nums1Unique:
                nums1Unique.remove(num)
        
        return [list(nums1Unique),list(nums2Unique)]