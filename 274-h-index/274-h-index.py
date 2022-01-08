class Solution:
    def hIndex(self, li: List[int]) -> int:
        h_idxs = []
        li = sorted(li,reverse=True)
        
        if li[0] == li[-1] == 1:
            return 1
        
        for h in range(len(li)):
            if li[h]<h+1:
                break
            h_idxs.append(h+1)
            

        return h_idxs[-1] if h_idxs != [] else 0
            
        