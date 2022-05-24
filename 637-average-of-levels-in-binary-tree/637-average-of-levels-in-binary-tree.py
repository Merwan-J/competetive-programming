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
        stack = collections.deque([root])
        temp = []
        count,total = 0,0
        res = [root.val/1]
        
        
        def friends(node):
            if node is None:
                return []
            ans = []
            if node.right: ans.append(node.right)
            if node.left: ans.append(node.left)
            
            return ans
        
        while stack:
            v = stack.popleft()
            
            for node in friends(v):
                temp.append(node)
                count += 1
                total += node.val
                
            if not stack:
                stack = collections.deque(temp)
                temp = []
                if count!=0: res.append(total/count)
                count,total = 0,0
        return res
        print(visited)



#         nodes = dict()
#         def dfs(node,depth):
#             if node is None:
#                 return 
#             depth += 1
#             nodes[depth] = nodes.get(depth,[])+[node.val]
#             dfs(node.right,depth)
#             dfs(node.left,depth)
#         dfs(root,0)
#         nodes = sorted(nodes.items())
#         nodes = [sum(item[1])/len(item[1]) for item in nodes]
        
#         return nodes