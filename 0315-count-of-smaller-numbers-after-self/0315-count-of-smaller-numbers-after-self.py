
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = SortedList()
        ans = [0]*n
        
        for i in range(n-1,-1,-1):
            num = nums[i]
            ans[i] = arr.bisect_left(num)
            arr.add(num)
            
        return ans
        