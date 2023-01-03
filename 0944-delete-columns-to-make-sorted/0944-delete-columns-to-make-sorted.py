class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        count = 0
        
        for c in range(col):
            prev = strs[0][c]

            for r in range(row):
                if ord(strs[r][c])<ord(prev):
                    count+=1
                    break
                prev = strs[r][c]
        
        return count
            
    ["r r j k",
     "f u r t",
     "g u z m"]