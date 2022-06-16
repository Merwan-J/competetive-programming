class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points) #number of nodes
        visited = [False]*n #to keep track of visited nodes
        heap = [] # to maintain the lowest cost edges
        graph = collections.defaultdict(list) # to store each edges of a given vertex
        getCost = lambda p1,p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) #calculate the cost of an edge
        mstcost = 0 #to keep track of the minimum cost
        
        for i in range(n):
            for j in range(i+1,n):
                cost = getCost(points[i],points[j])
                graph[i].append((cost,j))
                graph[j].append((cost,i))
        
        heap = graph[0]
        heapq.heapify(graph[0])
        visited[0]  = True
        
        
        while heap and n:
            cost,node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            mstcost += cost
            n-=1
        
            for edge in graph[node]:
                if not visited[edge[1]]:
                    heapq.heappush(heap,edge)
        
        return mstcost
            