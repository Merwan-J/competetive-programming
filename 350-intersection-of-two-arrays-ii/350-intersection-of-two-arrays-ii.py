class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map = dict()
        
        for i in nums1:
            Map[i] = Map.get(i,0)+1
        
        res = []
        for num in nums2:
            if num in Map and Map[num]>0:
                Map[num] -= 1
                res.append(num)
        return res
        