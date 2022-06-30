class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        unique = set()
        count = 0
        
        for num in nums:
            ans1,ans2 = tuple(sorted((num,num-k))),tuple(sorted((num,num+k)))
            
            if num-k in seen and ans1 not in unique:
                count += 1
                unique.add(ans1)
            
            if num+k in seen and ans2 not in unique:
                count += 1
                unique.add(ans2)
        
            seen.add(num)
        
        return count
        