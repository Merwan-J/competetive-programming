class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        
        for end,start in prereq:
            graph[start]+=[end]
            indegree[end]+=1
        
        q = deque([])
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            children = graph[node]
            for child in children:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        
        return sum(indegree) == 0
        
        
                