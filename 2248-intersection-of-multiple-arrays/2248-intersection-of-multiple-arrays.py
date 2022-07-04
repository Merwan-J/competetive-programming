class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = collections.defaultdict(int)
        
        for li in nums:
            for num in li:
                counter[num]+=1
        
        ans = []
        n = len(nums)
        for num,count in counter.items():
            if counter[num] == n:
                ans.append(num)
        
        return sorted(ans)