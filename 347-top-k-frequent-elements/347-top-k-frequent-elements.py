class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
#         hashMap = {}
#         count = 1
        
#         for num in nums:
#             hashMap[num] = hashMap.get(num,0) + 1

#         hashMap = dict(sorted(hashMap.items(),key=lambda item: item[1],reverse=True))
#         arr = []
        
#         for key,value in hashMap.items():
#             arr.append(key)
#             if len(arr)==k:
#                 return arr
        counter = dict()
    
        for i in nums:
            counter[i] = counter.get(i,0)+1
        ans = []
        for key,value in counter.items():
            ans.append((value,key))
        
        heapq.heapify(ans)
        
        while len(ans)>k:
            heapq.heappop(ans)
        
        for i in range(len(ans)):
            ans[i] = ans[i][1]
        return ans