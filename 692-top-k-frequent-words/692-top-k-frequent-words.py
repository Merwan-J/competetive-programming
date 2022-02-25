class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        
        arr = []
        
        heapq.heapify(arr)
        
        for key,value in counter.items():
            heapq.heappush(arr,(-value,key))
        
        ans = []
        
        while len(ans)<k:
            ans.append(heapq.heappop(arr)[1])
        
        return ans
        
        