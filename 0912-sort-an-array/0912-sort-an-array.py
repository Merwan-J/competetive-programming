class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        mn = min(nums)
        mx = max(nums)
        
        
        ans = []
        
        for num in range(mn,mx+1):
            if num in counter:
                ans += [num]*counter[num]
        
        return ans 
        