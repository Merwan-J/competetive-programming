class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
#         move the ones that have zero count to crntTrue and compare the length of it to the crnt set at each sliding window.... 
# the other naive way of doing it just by having crnt set being checked weather each elt's count is zero or not


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

            