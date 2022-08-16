class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.node = TrieNode()
        self.words = []
        
    def insert(self,word):
        flag = False
        cur = self.node
        
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                if i!=len(word)-1:
                    flag = True
                    break
                    
                else:
                    cur.children[char] = TrieNode()
                    cur.end = True
            cur = cur.children[char]
        
        if not flag:
            self.words.append(word)
            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        
        t = Trie()
        
        for word in words:
            t.insert(word)
        
        words = sorted(t.words,key=lambda item: (-len(item),item))
        
        return "" if words==[] else words[0]
        
        
        