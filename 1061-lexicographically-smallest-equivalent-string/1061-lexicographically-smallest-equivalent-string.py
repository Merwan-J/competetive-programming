class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = [i for i in range(26)]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
            
        def union(u,v):
            a = find(u)
            b = find(v)
            
            if a>b:
                a,b = b,a
            
            parent[b] = a
        
        for u,v in zip(s1,s2):
            u = ord(u) - ord('a')
            v = ord(v) - ord('a')
            union(u,v)

        ans = []
        
        for char in baseStr:
            char = ord(char)-ord('a')
            ans.append(chr(find(char)+ord('a')))
            
            
        
        return "".join(ans)
            
            