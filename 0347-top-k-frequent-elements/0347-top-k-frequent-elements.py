class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
                
        for num,count in counter.items():
            freq[count].append(num)
            
        ans = []
        for count in range(len(freq)-1,0,-1):
            for num in freq[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans 
        
        
        
        