class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set([-1,len(arr)])
        
        def dfs(node):
            if node in visited or node<0 or node>=len(arr):
                return False
            
            if arr[node] == 0:
                return True
    
            visited.add(node)
    
            return dfs(node-arr[node]) or dfs(node+arr[node])
        
        return dfs(start)