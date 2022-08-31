class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        graph = defaultdict(list)
        valid = lambda row,col: row>-1 and row<m and col>-1 and col<n
        
        indegree = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                num = matrix[row][col]
                up,down,right,left = [],[],[],[]
                for a,b in [(-1,0),(1,0),(0,1),(0,-1)]:
                    r,c = row+a,col+b
                    if valid(r,c) and num < matrix[r][c]:
                        graph[(row,col)] += [(r,c)]
                        indegree[r][c] += 1
        q = deque([])
        for row in range(m):
            for col in range(n):
                if indegree[row][col] == 0:
                    q.append((row,col))
        
        @cache
        def dfs(r,c):
            if graph[(r,c)] == []:
                return 1
            ans = 0
            for row,col in graph[(r,c)]:
                ans = max(ans,dfs(row,col))
            
            return 1 + ans
        
        ans = 0
        while q:
            r,c = q.popleft()
            ans = max(ans,dfs(r,c))
        
        return ans
            

               