class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph = collections.defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        leaves = [node for node,val in graph.items() if len(val)==1]
        
        while n>2:
            n-=len(leaves)
            
            newleaves = []
            
            while leaves:
                node = leaves.pop()
                adj = graph[node].pop()
                graph[adj].remove(node)
                
                if len(graph[adj])==1:
                    newleaves.append(adj)
            leaves = newleaves
        
        return leaves
            