class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(set)
        indegree = {i:0 for i in range(n)}
        
        for u,v in edges:
            graph[u].add(v)
            indegree[v]+=1
            
        zeros = [node for node,count in indegree.items() if count==0]
        ancestors = {i:set() for i in range(n)}
        
        while zeros:
            node = zeros.pop()
            thisAncestors = ancestors[node]
            # print(node,thisAncestors,graph[node])
            for adj in graph[node]:
                indegree[adj]-=1
                ancestors[adj].add(node)
                ancestors[adj].update(thisAncestors) 
                # print(node,adj,ancestors[adj])
                if indegree[adj]==0:
                    zeros.append(adj)
        
        return [sorted(list(val)) for key,val in ancestors.items()]
