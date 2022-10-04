class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        check = False
        unique = ""

        def dfs(n, curstring): # n = 3
            nonlocal check, unique
            if n == 0:
                if curstring not in nums: 
                    check = True
                    unique = curstring
                return 

            if not check:
                dfs(n - 1, curstring + "1")
            if not check:
                dfs(n - 1, curstring + "0")

        dfs(len(nums), "")
        return unique