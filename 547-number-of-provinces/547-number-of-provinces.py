class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        visited = []
        def dfs(id):
            visited.append(id)
            for i in range(len(isConnected[id])):
                if i not in visited and isConnected[id][i]==1:
                    dfs(i)
        
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces