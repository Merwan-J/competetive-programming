class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
#         count = 0
        
#         for i in range(len(fruits)):
#             total = 0
#             next = -1
#             for j in range(i,len(fruits)):
#                 if fruits[j]!=fruits[i] and next ==-1:
#                     next = fruits[j]
#                 if fruits[j]==fruits[i] or (next!=-1 and fruits[j]==next):
#                     total+=1
#             count = max(count,total)
        
#         return count

        count = 0
        l,r = 0,0
        
        hashMap = dict()
        
        
        while r<len(fruits):
            hashMap[fruits[r]] = r
            
            if len(hashMap) > 2:
                last = len(fruits)-1
                for key,value in hashMap.items():
                    last = min(last,value)
                l = last+1
                hashMap.pop(fruits[last])
            
            count = max(count,r-l+1)
            r+=1
                
        
        return count