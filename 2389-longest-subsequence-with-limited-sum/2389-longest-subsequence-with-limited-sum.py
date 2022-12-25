class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        psum = [0]
        
        for num in nums:
            psum.append(psum[-1] + num)
        
        ans = []
        
        for num in queries:
            ans.append(bisect_right(psum,num)-1)
        
        return ans