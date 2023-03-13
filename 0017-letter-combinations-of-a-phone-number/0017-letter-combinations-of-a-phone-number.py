class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {2:'abc',3:'def',4:'ghi',
                        5:'jkl',6:'mno',7:'pqrs',
                        8:'tuv',9:'wxyz'}
        
        ans = []
        path = []
        
        
        def backtrack(i,digits):
            if i == len(digits):
                if path:ans.append("".join(path))
                return 
            
            for char in combinations[int(digits[i])]:
                path.append(char)
                backtrack(i+1,digits)
                path.pop()
        
        backtrack(0,digits)
        return ans 