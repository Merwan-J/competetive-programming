class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        visited = {}
        username = {}
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            parentMail = account[1]
            
            for email in emails:
                
                username[email] = name
                graph.setdefault(email,set()).add(parentMail)
                graph.setdefault(parentMail,set()).add(email)
                
            
        # print(graph)
        
        def dfs(node):
            if node in visited:
                return []
            
            visited[node] = True
            ans = [node]
            
            for adj in graph[node]:
                ans += dfs(adj)
            
            return ans
        
        output = []
        for email,name in username.items():
            if email not in visited:
                output.append([name]+sorted(dfs(email)))
        
        return output