class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([source])
        visited = set()
        
        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            visited.add(node)
            
            for adj in graph[node]:
                if adj not in visited:
                    q.append(adj)
        return False