# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
#         stack = collections.deque([root])
#         visited = []
#         def friends(node):
#             if node is None:
#                 return []
#             ans = []
#             if node.right: ans.append(node.right)
#             if node.left: ans.append(node.left)
            
#             return ans
        
#         while stack:
#             v = stack.popleft()
#             # visit(v)
#             visited.append(v.val)
            
#             for node in friends(v):
#                 if node.val not in visited:
#                     stack.append(node)
#         print(visited)
        nodes = dict()
        def dfs(node,depth):
            if node is None:
                return 
            depth += 1
            nodes[depth] = nodes.get(depth,[])+[node.val]
            dfs(node.right,depth)
            dfs(node.left,depth)
        dfs(root,0)
        nodes = sorted(nodes.items())
        nodes = [sum(item[1])/len(item[1]) for item in nodes]
        
        return nodes