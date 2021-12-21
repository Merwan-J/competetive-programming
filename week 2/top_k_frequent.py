class Solution:
    def topKFrequent(self, li: List[int], k: int) -> List[int]:
        
        d = {}
        
        for i in li:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        
        li = []
        i=0
        
        for i in d:
            li.append(i)
        
        return li[:k]
            
            
