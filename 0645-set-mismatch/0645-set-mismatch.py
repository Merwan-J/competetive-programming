class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        
        for num in nums:
            if num in seen:
                ans.append(num)
            seen.add(num)
        
        for num in range(1,len(nums)+1):
            if num not in seen:
                ans.append(num)
                return ans
        