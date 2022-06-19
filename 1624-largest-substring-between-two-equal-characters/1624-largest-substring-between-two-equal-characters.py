class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {}
        ans = -1
        
        for i in range(len(s)):
            char = s[i]
            if char in hashmap:
                ans = max(ans,i-hashmap[char]-1)
            else:
                hashmap[char] = i
        
        return ans