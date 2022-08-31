class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for end,start in prereq:
            graph[start] += [end]
            indegree[end]+=1
            
        q = deque([])
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        if len(q)==0:
            return []
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            children = graph[node]
            for child in children:
                indegree[child]-=1
                if indegree[child] == 0:
                    q.append(child)
        
        return ans if len(ans)==numCourses else []
        
        