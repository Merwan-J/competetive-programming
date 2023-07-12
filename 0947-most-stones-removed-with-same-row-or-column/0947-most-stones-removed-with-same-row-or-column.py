class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        size = [1] * n 
        parents = [i for i in range(n)]
        
        
        def find(stone):
            if stone == parents[stone]:
                return stone 
            parents[stone] = find(parents[stone])
            return parents[stone]
        
        def union(u,v):
            a = find(u)
            b = find(v)
            
            if size[a] < size[b]:
                a,b = b,a 
            
            parents[b] = a
            size[a]+=size[b]
        
        
        for i in range(n):
            x1,y1 = stones[i]
            for j in range(i+1,n):
                x2,y2 = stones[j]
                
                if (x1==x2 or y1 == y2) and find(i) != find(j):
                    union(i,j)

        parents = [find(i) for i in parents]
        
        total = 0
        for stone in range(n):
            if parents[stone] == stone and size[stone]>1:
                total+=size[stone]-1
        
        return total
        