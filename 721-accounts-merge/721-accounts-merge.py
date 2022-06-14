class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    
    def find(self,child):
        if child == self.parents[child]:
            return child
        self.parents[child] = self.find(self.parents[child])
        return self.parents[child]
    
    def union(self,child,parent):
        self.parents[self.find(child)] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        
        #       DEPTH FIRST SEARCH METHOD
            
#         graph = {}
#         visited = {}
#         username = {}
        
#         for account in accounts:
#             name = account[0]
#             emails = account[1:]
#             parentMail = account[1]
            
#             for email in emails:
#                 username[email] = name
#                 graph.setdefault(email,set()).add(parentMail)
#                 graph.setdefault(parentMail,set()).add(email)
                
        
#         def dfs(node):
#             if node in visited:
#                 return []
            
#             visited[node] = True
#             ans = [node]
            
#             for adj in graph[node]:
#                 ans += dfs(adj)
            
#             return ans
        
#         output = []
#         for email,name in username.items():
#             if email not in visited:
#                 output.append([name]+sorted(dfs(email)))
        
#         return output




#               UNION FIND METHOD
        uf = UF(len(accounts))
    
        visited = {}
        
        for i,(name,*emails) in enumerate(accounts):
            for email in emails:
                if email in visited:
                    uf.union(i,visited[email])
                visited[email] = i
        
        ans = collections.defaultdict(list)
        for email,parent in visited.items():
            ans[uf.find(parent)].append(email)
        
        return [[accounts[i][0]]+sorted(emails) for i,emails in ans.items()]
            
    