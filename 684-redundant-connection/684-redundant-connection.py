class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
    def find(self,child):
        if child == self.parents[child]:
            return child
        self.parents[child] = self.find(self.parents[child])
        return self.parents[child]
    def union(self,node1,node2):
        n1p = self.find(node1)
        n2p = self.find(node2)
        
        if self.rank[n1p]==self.rank[n2p]:
            self.parents[n1p] = n2p
            self.rank[n2p]+=1
        elif self.rank[n1p]>self.rank[n2p]:
            self.parents[n2p] = n1p
        else:
            self.parents[n1p] = n2p
                    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges)+1)
        ans = []
        for u,v in edges:
            if uf.find(u) == uf.find(v):
                ans.append([u,v])
                continue
            uf.union(u,v)
        
        return ans[-1]