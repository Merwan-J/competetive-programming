class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        
        freq = {}
        minimum_elts_to_remove = float("inf")

        for i, num in enumerate(nums):
            if num in freq:
                minimum_elts_to_remove = min(minimum_elts_to_remove, (i - freq[num]) + 1)
            freq[num] = i

        return minimum_elts_to_remove if minimum_elts_to_remove != float("inf") else -1