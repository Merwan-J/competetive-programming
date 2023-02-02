class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(list(set(nums) - {0}))
