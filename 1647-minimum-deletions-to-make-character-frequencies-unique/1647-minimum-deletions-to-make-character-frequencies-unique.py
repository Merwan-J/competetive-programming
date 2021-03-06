class Solution:
    def minDeletions(self, s: str) -> int:
        
#         This is O(NlogN) solution
#         counter = collections.Counter(s)
        
#         counter = list(counter.values())
#         counter.sort(reverse=True)
#         count = 0
#         for i in range(1,len(counter)):
#             if counter[i-1]<=counter[i]:
#                 diff = abs(counter[i-1]-counter[i])
#                 diff = diff+1 if counter[i-1]!=0 else diff
#                 counter[i] = counter[i]-diff
#                 count += diff
        
#         return count
    
    
    
#         This is O(n)
        counter = collections.Counter(s)
        
        counter = list(counter.values())
        unique = set()
        count = 0
        
        for num in counter:
            while num in unique and num>0:
                num-=1
                count+=1
            unique.add(num)
        
        return count
        
        