class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.words = 0

class Trie:
    def __init__(self):
        self.node = TrieNode()
        
    def insert(self,word):
        cur = self.node
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.words+=1

        cur.isEnd = True
        
    def get(self,word):
        cur = self.node
        
        for char in word:
            if char not in cur.children:
                print("not here")
                return 0
            cur = cur.children[char]
        return cur.words
    
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        t = Trie()
        for word in words:
            t.insert(word)
        return t.get(pref)