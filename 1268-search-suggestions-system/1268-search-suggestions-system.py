# class Trie:
#     def __init__(self):
#         self.nodes = defaultdict(Trie)
#         self.word = None
    
#     def insert(self,word):
#         cur = self
#         for char in word:
#             cur = cur.nodes[char]
#         cur.word = word
    
#     def getWords(self):
#         words = []
        
#         def dfs(root):
#             if len(words)==3:
#                 return
#             if root.word:
#                 words.append(root.word)
            
#             for char in ascii_lowercase:
#                 if char in root.nodes:
#                     dfs(root.nodes[char])
            
#         dfs(self)
#         return words

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         trie = Trie()
#         for word in products:
#             trie.insert(word)
        
#         ans = []
#         cur = trie
#         for char in searchWord:
#             if cur is not None and char in cur.nodes:
#                 cur = cur.nodes[char]
#                 ans.append(cur.getWords())
#             else:
#                 cur = None
#                 ans.append([])
#         return ans          

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []
            
            def add_sugestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result