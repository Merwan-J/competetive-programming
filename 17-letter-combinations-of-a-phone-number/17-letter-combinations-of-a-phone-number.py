class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {2:'abc',3:'def',4:'ghi',
                        5:'jkl',6:'mno',7:'pqrs',
                        8:'tuv',9:'wxyz'}
        
        self.ans = []
        def helper(digits,s,i):
            if digits[i:] == "":
                if s: self.ans.append(s)
                return
            
            for char in combinations[int(digits[i])]:
                helper(digits,s+char,i+1)
        
        helper(digits,"",0)
        return self.ans
                   