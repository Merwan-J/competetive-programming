class WordDictionary:

    def __init__(self):
        self.nodes = dict()
        self.flag = False

    def addWord(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = WordDictionary()
            cur = cur.nodes[char]
        cur.flag = True
    
            
    def search(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                word = word[i+1:]
                for char,node in cur.nodes.items():
                    if node.search(word):
                        return True
                return False
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return cur.flag == True
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)