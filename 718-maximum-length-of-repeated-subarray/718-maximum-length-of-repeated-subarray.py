class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
#         self.ans = 0
#         @lru_cache()
#         def dfs(l,r):
#             if l==len(nums1) or r==len(nums2):
#                 return 0
            
#             dfs(l,r+1)
#             dfs(l+1,r)
            
#             common = 0 if nums1[l] != nums2[r] else 1 + dfs(l+1,r+1)
#             self.ans = max(self.ans, common)
#             return common
            
            
#         dfs(0,0)
#         return self.ans
    
        ans = 0
        dp = [[0 for _ in range(len(nums2))] for i in range(len(nums1))]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1
                    if i-1>=0 and j-1>=0:
                        dp[i][j]+=dp[i-1][j-1]
                    ans = max(ans,dp[i][j])
        return ans
            
        