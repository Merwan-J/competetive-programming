class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        arr = sorted((ages[i],scores[i]) for i in range(n))
        dp = [score for age,score in arr]
        
        for i in range(n):
            for j in range(i):
                if arr[i][1]>=arr[j][1]:
                    dp[i] = max(dp[j]+arr[i][1],dp[i])
        
        return max(dp)