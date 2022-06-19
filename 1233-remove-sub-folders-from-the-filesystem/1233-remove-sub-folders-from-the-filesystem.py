class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.word = None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,folders):
        
        ans = []
        
        for folder in folders:
            root = self.root
            seen = False
            
            for word in folder.split('/')[1:]:
                if root.word:
                    seen = True
                    break
                if word not in root.nodes:
                    root.nodes[word] = TrieNode()
                root = root.nodes[word]
            if not seen:
                ans.append(folder)
                root.word = folder
        return ans
    
                
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))    
#         ans = set()
        
#         for f in folder:
#             for i in range(1, len(f)):
#                 if f[i] == '/' and f[: i] in ans:
#                     break
#                 if i==len(f)-1:
#                     ans.add(f)
        
#         return list(ans)

        return Trie().insert(folder)
    
        