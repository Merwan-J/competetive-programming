class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = sum(nums)
        mn = min(nums)
        n = len(nums)
        return total-mn*n