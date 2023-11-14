# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # node.val = number of nodes in cur level - number of children of its parent node 
        # count children of a node
        # count nodes in a level
        # track level
        
        children = defaultdict(int)
        levelSum = defaultdict(int)
        
        q = [(root,-1)]
        level = 1
        
        children[-1] = root.val
        levelSum[1] = root.val
        
        
        while q:
            n = len(q)
            curLevel = []
            
            for _ in range(n):
                node,parent = q.pop()
                node.val = levelSum[level]-children[parent]
                
                if node.right: 
                    curLevel.append((node.right,node))
                    children[node]+=node.right.val
                    levelSum[level+1]+=node.right.val
                    
                if node.left: 
                    curLevel.append((node.left,node))
                    children[node]+=node.left.val
                    levelSum[level+1]+=node.left.val
            
            q = curLevel
            level+=1
        
        return root 
                    
        
        
        
        
        
        
        
         