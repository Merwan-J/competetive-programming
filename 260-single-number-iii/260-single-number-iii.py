class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        
        ans = []
        for num,count in counter.items():
            if count == 1:
                ans.append(num)
        
        return ans