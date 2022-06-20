class SuffixNode:
    def __init__(self):
        self.nodes = dict()
        self.indices = set()

class PrefixNode:
    def __init__(self):
        self.nodes = dict()
        self.indices = []
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.proot = PrefixNode()
        self.sroot = SuffixNode()
        
        for i,word in enumerate(words):
#             insertion for the prefix
            pcur = self.proot
            
            for char in word:
                if char not in pcur.nodes:
                    pcur.nodes[char] = PrefixNode()
                pcur = pcur.nodes[char]
                pcur.indices.append(i)
            
#             insertion for the suffix:
            
            word = word[::-1]
            scur = self.sroot
            
            for char in word:
                if char not in scur.nodes:
                    scur.nodes[char] = SuffixNode()
                scur = scur.nodes[char]
                scur.indices.add(i)

    def f(self, prefix: str, suffix: str) -> int:
        pcur = self.proot
        for char in prefix:
            if char not in pcur.nodes:
                return -1
            pcur = pcur.nodes[char]
        
        scur = self.sroot
        suffix = suffix[::-1]
        
        for char in suffix:
            if char not in scur.nodes:
                return -1
            scur = scur.nodes[char]
        
        presult = pcur.indices
        sresult = scur.indices
        
#         here is the trick, without it it would go TLE
        for i in range(len(presult)-1,-1,-1):
            if presult[i] in sresult:
                return presult[i]
        return -1
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)