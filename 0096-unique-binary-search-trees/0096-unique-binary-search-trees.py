class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dfs(nodes):
            if len(nodes) == 0:
                return 0
            
            nodes = list(nodes)
            
            ans = 0
            for i,node in enumerate(nodes):
                left = dfs(tuple(nodes[:i]))
                right = dfs(tuple(nodes[i+1:]))
                
                if left == 0 and right == 0:
                    ans+=1
                elif left == 0 or right == 0:
                    ans+=max(left,right)
                else:
                    ans+=right*left
                
            return ans
        
        nodes = tuple([node for node in range(1,n+1)])
        
        return dfs(nodes)
            