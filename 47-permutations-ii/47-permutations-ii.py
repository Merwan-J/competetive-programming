class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        
        def dfs(s,counter):
            if len(s) == len(nums):
                self.ans.append(s.copy())
                return
            
            for num,count in counter.items():
                if count>0:
                    s.append(num)
                    counter[num]-=1
                    dfs(s,counter)
                    s.pop()
                    counter[num]+=1
            
        dfs([],Counter(nums))
        
        return self.ans
            
            
            