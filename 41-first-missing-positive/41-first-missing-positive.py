class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        the concept behind this question is pretty good.
        one can come up with it if given some time; basically from observation we know that the answer belongs in the range [1,n+1] where n is the length of the given nums array
        for example consider the array [1,2,3,4] n = 4
        we know that the first missing positive is in [1,n+1->5], since 1-4 is present that makes the answer 5
        
        """
        nums.append(0)
        n = len(nums)
        
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=len(nums):
                nums[i] = 0
                
        for i in range(len(nums)):
            nums[nums[i]%n] += n
            
        for i in range(1,len(nums)):
            if nums[i]//n == 0:
                return i
        
        return n
            