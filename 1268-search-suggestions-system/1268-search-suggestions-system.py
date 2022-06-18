class Trie:
    def __init__(self):
        self.nodes = defaultdict(Trie)
        self.word = None
    
    def insert(self,word):
        cur = self
        for char in word:
            cur = cur.nodes[char]
        cur.word = word
    
    def getWords(self):
        words = []
        
        def dfs(root):
            if len(words)==3:
                return
            if root.word:
                words.append(root.word)
            
            for char in ascii_lowercase:
                if char in root.nodes:
                    dfs(root.nodes[char])
            
        dfs(self)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.insert(word)
        
        ans = []
        cur = trie
        for char in searchWord:
            if cur is not None and char in cur.nodes:
                cur = cur.nodes[char]
                ans.append(cur.getWords())
            else:
                cur = None
                ans.append([])
        return ans                