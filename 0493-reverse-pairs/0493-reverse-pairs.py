from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = SortedList()
        count = 0
        
        for num in nums:
            count += len(arr) - arr.bisect_right(2*num)
            arr.add(num)
        
        return count 