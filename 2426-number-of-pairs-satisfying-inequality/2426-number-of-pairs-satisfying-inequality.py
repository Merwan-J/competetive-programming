from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = SortedList()
        count = 0
        
        for num1,num2 in zip(nums1,nums2):
            count+=arr.bisect_right(num1-num2+diff)
            arr.add(num1-num2)
        
        return count