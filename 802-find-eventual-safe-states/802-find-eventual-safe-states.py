class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        parents = defaultdict(list)
        outdegree = [0]*len(graph)
        terminals = deque([])
        safe = [False]*len(graph)
        
        for node,friends in enumerate(graph):
            if friends == []:
                safe[node] = True
                terminals.append(node)
                
        for parent,children in enumerate(graph):
            for child in children:
                parents[child]+=[parent]
                outdegree[parent]+=1
        
        
        while terminals:
            node = terminals.popleft()
            for parent in parents[node]:
                outdegree[parent]-=1
                if outdegree[parent] == 0:
                    safe[parent] = True
                    terminals.append(parent)
        
        return [node for node,isSafe in enumerate(safe) if isSafe]
                    
        
        
        
        
                
        
        
        
                