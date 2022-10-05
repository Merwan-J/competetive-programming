class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        numsset = set(nums)
        self.ans = "" # assuming you submit it in leetcode 
        def backTrack(s,target_len):
            if len(s) == target_len:
                if s not in numsset:
                    self.ans = s
                return

            backTrack(s+"0",target_len)
            backTrack(s+"1",target_len)

        backTrack("",len(nums))
        return self.ans