class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(lambda: 1)

        def check(word):
            maxLen = 1
            for j in range(len(word)):
                s = word[:j] + word[j+1:]
                if s in dp:
                    maxLen = max(maxLen, dp[s]+1)
            return maxLen

        for word in sorted(words, key=len):
            dp[word] = check(word)

        return max(dp.values())