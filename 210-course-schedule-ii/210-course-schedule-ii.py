class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adjList = [[]]*numCourses
        zeroInDegree = []
        inDegree = [0]*numCourses
        topoSort = []
        
        for pair in prereq:
            a = pair[0]
            b = pair[1]
            
            adjList[b] = adjList[b] + [a]
            inDegree[a]+=1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroInDegree.append(i)
        

        print(adjList,inDegree,zeroInDegree)

        while zeroInDegree:
            cur = zeroInDegree.pop()
            topoSort.append(cur)
            
            for i in adjList[cur]:
                inDegree[i]-=1
                
                if inDegree[i] == 0:
                    zeroInDegree.append(i)
        
        return topoSort if sum(inDegree)==0 else []
