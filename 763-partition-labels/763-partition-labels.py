class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        counter = dict()
        partitions = []
        
        for i in range(len(s)):
            counter[s[i]] = i
        
        l,r = 0,0
        
        while r<len(s):
            go = counter[s[r]]
            
            while r<go:
                go = max(counter[s[r]],go)
                r+=1
            
            partitions.append(r-l+1)
            
            r+=1
            l=r
        
        
        return partitions

            