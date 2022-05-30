class Solution:
    def jump(self, nums: List[int]) -> int:
        lastMaxJumped = currentMaxJump = count = 0
        
        for i in range(len(nums)-1):
            currentMaxJump = max(currentMaxJump,i + nums[i])
            if i==lastMaxJumped:
                lastMaxJumped = currentMaxJump
                count += 1
        
        return count
                