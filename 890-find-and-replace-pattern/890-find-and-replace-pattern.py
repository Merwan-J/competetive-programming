class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        visited = set()
        hmap = dict()
        ans = []
        count = collections.Counter(pattern)
        
        for word in words:
            flag = True
            for i in range(len(word)):
                if len(word) != len(pattern):
                    break
                char = word[i]
                if pattern[i] in visited and not(hmap.get(char,-1) == pattern[i]):
                    flag = False
                    break
                elif pattern[i] not in visited and char in hmap:
                    flag = False
                    break
                visited.add(pattern[i])
                hmap[char] = pattern[i]
            
            if flag:
                ans.append(word)
            hmap = {}
            visited = set()
        
        return ans
                
    
    