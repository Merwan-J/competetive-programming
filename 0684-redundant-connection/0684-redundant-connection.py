class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1]*(n+1)
        
        def find(node):
            if parent[node] == node:
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
            
        
        ans = set()
        
        for u,v in edges:
            if find(u) == find(v):
                ans.add((u,v))
            else:
                union(u,v)
        
        for u,v in reversed(edges):
            if (u,v) in ans:
                return [u,v]
        

        
        
            