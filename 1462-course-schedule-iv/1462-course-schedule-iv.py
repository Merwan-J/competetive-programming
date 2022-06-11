class Solution:
    def checkIfPrerequisite(self, numCourses: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        outdegree = collections.defaultdict(set)
        for i in range(len(prereq)):
            req = prereq[i][0]
            course = prereq[i][1]
            
            outdegree[req].add(course)
        
        # print(outdegree)
        
        indirect = {}
        
        def dfs(node):
            if not outdegree[node]:
                indirect[node] = set()
                return indirect[node]
            
            if node in indirect:
                return indirect[node]
            
            ans = outdegree[node].copy()
            
            for course in outdegree[node]:
                ans.update(dfs(course))
            
            indirect[node] = ans
            
            return indirect[node]
        
        for course in range(numCourses):
            dfs(course)
        
        ans = []
        for req,course in queries:
            if course in indirect[req]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
            
                
            