class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(list)
        count = 0
        
        for i in range(len(nums)):
            if nums[i] in seen:
                for index in seen[nums[i]]:
                    count = count + 1 if (index*i)%k==0 else count
            seen[nums[i]].append(i)
        return count