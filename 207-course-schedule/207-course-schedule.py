class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
#         Topological sort
        adjList = [[]]*numCourses
        zeroInDegree = []
        inDegree = [0]*numCourses
#     make adj list for each course
        for pair in prereq:
            a = pair[0]
            b = pair[1]
            
            adjList[b] = adjList[b] + [a]
            inDegree[a]+=1
        
#   populate the zeroInDegree llist
        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroInDegree.append(i)
        

        print(adjList,inDegree,zeroInDegree)
#   loop over the zeroindegree decrementing the total egdes and appending zeroindegrees along the way
        while zeroInDegree:
            cur = zeroInDegree.pop()
            for i in adjList[cur]:
                inDegree[i]-=1
                
                if inDegree[i] == 0:
                    zeroInDegree.append(i)
        
# check if we have traversed all the nodes in topological manner
        return sum(inDegree)==0


        