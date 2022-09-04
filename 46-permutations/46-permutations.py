class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        def dfs(s):
            if len(s) == len(nums):
                self.ans.append(s.copy())
                return
            
            for num in nums:
                if num not in s:
                    s.append(num)
                    dfs(s)
                    s.pop()
            
        dfs([])
        return self.ans