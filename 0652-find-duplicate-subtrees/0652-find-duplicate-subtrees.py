# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        lookup = defaultdict(set)
        self.ans = set()
        self.seen = set()
        
        def dfs(node):
            if node is None:
                return (None,)
            
                
            
            left = dfs(node.left)
            right = dfs(node.right)
            subtree = left + (node.val,) + right
            
            if node.right is None and node.left is None:
                subtree = (node.val,)
            
            if node.val in lookup and subtree in lookup[node.val] and subtree not in self.seen:
                self.ans.add(node)
                self.seen.add(subtree)
            
            lookup[node.val].add(subtree)
            return subtree
        
        dfs(root)
        return self.ans