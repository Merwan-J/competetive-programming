class Trie:

    def __init__(self):
        self.links = dict()
        self.flag = False
    

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.links:
                cur.links[char] = Trie()
            cur = cur.links[char]
        
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            if char not in cur.links:
                return False
            cur = cur.links[char]
            
        return cur.flag == True

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            if char not in cur.links:
                return False
            cur = cur.links[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)