class TrieNode:
    def __init__(self):
        self.children  = {}
        self.end = False
        self.words = []
class Trie:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self,word):
        cur = self.node
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
        cur.words.append(word)
    
    def get(self,word):
        if word[0] not in self.node.children:
            return word
        
        cur = self.node
        for char in word:
            if char not in cur.children:
                break
            if cur.end:
                break
            cur = cur.children[char]
        
        if cur.end:
            return cur.words[0]
        return word
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent = sentence.split()


        t = Trie()
        for word in dictionary:
            t.insert(word)   
        
        ans = []        
        for word in sent:
            ans.append(t.get(word))
            
        return ' '.join(ans)
        