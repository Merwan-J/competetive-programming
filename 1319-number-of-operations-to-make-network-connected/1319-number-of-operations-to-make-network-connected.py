class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1]*n
        
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(u,v):
            a = find(u)
            b = find(v)
            
            if size[a]<size[b]:
                a,b = b,a
            
            size[a]+=size[b]
            parent[b] = a
        
        
        spare = 0
        
        for u,v in connections:
            if find(u) == find(v):
                spare+=1
                continue
            union(u,v)
        
        groups = sum([1 if i == find(i) else 0 for i in range(n)])
        # print([find(i) for i in range(n)])
        return groups -1 if groups-1<=spare else -1
        