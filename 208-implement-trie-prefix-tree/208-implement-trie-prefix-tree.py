class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end == True

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)