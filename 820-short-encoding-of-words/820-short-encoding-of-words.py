class TrieNode:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.Ends = []
    
    def insert(self,word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        self.Ends.append((root,len(word)+1))
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = Trie()
                
        for word in words:
            trie.insert(word[::-1])

        return sum(val for node,val in trie.Ends if len(node.children)==0)