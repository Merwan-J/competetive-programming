class Solution:
    def findBestValue(self, nums: List[int], target: int) -> int:
#         https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/JavaC%2B%2BPython-Just-Sort-O(nlogn)

# this is the best solution so far... 



        nums.sort()
        running_sum = 0
        remaining = len(nums)
        for num in nums:
            if running_sum + remaining * num > target:
                 # (target - 0.0001) is done to consider the case where both lower ceiling and higher ceiling int is equally away from the target.
                return int(round((target - running_sum-0.0001) / remaining))
            running_sum += num
            remaining -= 1
            
        return nums[-1]
        