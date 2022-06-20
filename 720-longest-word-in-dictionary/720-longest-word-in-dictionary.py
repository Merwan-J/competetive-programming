class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,words):
        ans = set()
        
        for word in words:
            root = self.root
            lastWord = None
            add = True
            
            for i in range(len(word)):
                char = word[i]
                if char not in root.nodes and i==len(word)-1:
                    root.nodes[char] = TrieNode()
                elif char not in root.nodes and i!= len(word)-1:
                    add = False
                    break
                    
                root = root.nodes[char]
                
                if root.word:
                    lastWord = root.word
            # print(word,add)
            if add:
                root.word = word
                ans.add(word)
                
                if lastWord and lastWord in ans: 
                    ans.remove(lastWord)
                
            
            
        
        ans = sorted(list(ans),key=lambda i: len(i),reverse=True)
        return ans
            
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        # print(words)
        
        ans = Trie().insert(words)
        longest = ans[0] if ans else ""
        # print(ans)
        
        for word in ans:
            if len(word) == len(longest) and word<longest:
                longest = word
                
        return longest
        
        