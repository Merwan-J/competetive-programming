class Solution:
    def frequencySort(self, s: str) -> str:
        hash = dict()
        
        for char in s:
            hash[char] = hash.get(char,0) + 1
        
        hash = dict(sorted(hash.items(),key=lambda item: item[1],reverse=True))
        ans = ""
        for key,value in hash.items():
            ans += key*value
        
        return ans