class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
#         abcabcbb
#  |a| |ab| |abc| |abca|X |bca| |bcab|X  |cab| |cabc|X |abc| 
#  |abcb|X |bcb|X |cb| |cbb|X |bb|X |b| -> r==len(string) breaks

#   bbbbb
#   |b| |bb|X  |b| |bb|X |b|  |bb|X |b| |bb|X |b| ->r==len(string)


#           pwwkew
# |p| |pw| |pww|X  |ww|X |w|  |wk|  |wke| |wkew| |kew|-> r==len(string)

        hash = {s[0]:1}
        l,r = 0,1
        count = 1
        
        while r<len(s):
            if s[r] in hash and hash[s[r]]!=0:
                count = max(count,r-l)
                hash[s[l]] -= 1
                l+=1
                continue
            elif (s[r] in hash and hash[s[r]]==0) or s[r] not in hash:
                hash[s[r]] = hash.get(s[r],0) + 1
                r+=1
                count = max(count,r-l)
        
        return count
            

                