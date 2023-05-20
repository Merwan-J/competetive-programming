class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        f = defaultdict(int)

        nums = set(nums)

        for num in nums:

            f[num] += 1


        max_length = 0

        for num in nums:

            if f[num-1] == 0 :

                length = 0
                while f[num] > 0:

                    length += 1
                    num += 1

                max_length = max(max_length,length)

        return max_length