class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         UNION FIND METHOD
        n = len(isConnected)
        parents = [i for i in range(n)]
        rank = [0]*n
        
        count = n
        
        def findParent(node):
            if parents[node] == node:
                return node
            parents[node] = findParent(parents[node])    
            return parents[node]
        
        for node in range(n):
            for adj in range(n):
                if isConnected[node][adj]==0:
                    continue
                    
                nodeP = findParent(node)
                adjP = findParent(adj)
                
                if nodeP == adjP:
                    continue
                else:
                    if rank[nodeP]==rank[adjP]:
                        parents[adjP] = nodeP
                        rank[nodeP]+=1
                    elif rank[nodeP] > rank[adjP]:
                        parents[adjP] = nodeP
                    elif rank[adjP] > rank[nodeP]:
                        parents[nodeP] = adjP
                    count-=1
        
        return count
    
# #       DFS METHOD
#         visited = []
#         def dfs(id):
#             visited.append(id)
#             for i in range(len(isConnected[id])):
#                 if i not in visited and isConnected[id][i]==1:
#                     dfs(i)
        
#         provinces = 0
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 dfs(i)
#                 provinces += 1
        
#         return provinces
