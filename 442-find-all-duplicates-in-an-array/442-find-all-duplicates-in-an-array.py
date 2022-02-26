class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        count = 0
        for key,value in counter.items():
            if value==2:
                nums[count] = key
                count+=1
        
        while len(nums)>count:
            nums.pop()
        
        return nums
            