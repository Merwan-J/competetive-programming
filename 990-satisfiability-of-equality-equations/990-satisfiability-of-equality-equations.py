class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        notequals = defaultdict(set)
        graph = defaultdict(list)
        
        for eqn in equations:
            x,opp,y = eqn[0],eqn[1],eqn[3]
            
            if opp == "=":
                graph[x] +=[y]
                graph[y] +=[x]
            else:
                if x == y:
                    return False
                
                notequals[x].add(y)
                notequals[y].add(x)
        
        def dfs(node,visited): 
            if node in visited:
                return True
            
            visited.add(node)
            
            ans = True
            
            for friend in graph[node]:
                for enemy in notequals[node]:
                    if enemy in visited:
                        return False
                if friend not in visited:
                    ans = ans and dfs(friend,visited)
                    
            return ans
        
        for node in graph:
            ans = dfs(node,set())
            if ans == False:
                return False
        
        return True
            