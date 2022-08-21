class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        def permute(s):
            if len(s) == len(nums):
                self.ans.append(s)
                return
            
            for num in nums:
                if num not in s:
                    new = s + [num]
                    permute(new)
        
        permute([])
        
        return self.ans
        