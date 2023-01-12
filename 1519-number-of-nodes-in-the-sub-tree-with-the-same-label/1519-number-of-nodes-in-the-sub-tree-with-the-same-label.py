class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        # define a fuc
        # have global ans array of size n
        # for each children of the node give them countery array of size 26
        # for each return array from the children merge them
        # update ans array
        # return the merged array
    
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        ans = [0]*n
        
        def dfs(node,parent,arr):
            if node is None:
                return arr
            
            curAns = [0]*26
            curAns[ord(labels[node])-ord('a')]+=1
            
            for adj in graph[node]:
                if adj != parent:
                    response = dfs(adj,node,[0]*26)
                    curAns = [curAns[i]+response[i] for i in range(26)]
            
            ans[node] = curAns[ord(labels[node])-ord('a')]
            return curAns
        
        dfs(0,-1,[0]*26)
        return ans
            
            
        