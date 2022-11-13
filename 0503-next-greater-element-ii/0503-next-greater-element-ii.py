class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        fake = [i for i in range(n)]
        fake+=fake
        
        ans = [-1]*n
        stack = []
        
        for i in range(len(fake)):
            idx = fake[i]
            num = nums[idx]
            
            while stack and num>nums[stack[-1]]:
                poppedIdx = stack.pop()
                if ans[poppedIdx]==-1:
                    ans[poppedIdx] = num
                    
            stack.append(idx)
        
        return ans
            
        
        