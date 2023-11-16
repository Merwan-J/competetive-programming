# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def preorder(node):
            if node is None:
                ans.append("*")
                return
            
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        ans = ",".join(ans)
        # print(ans)
        return ans 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(',')
        
        def rev(i):
            if data[i]=="*":
                return (1,None)
            root = TreeNode(int(data[i]))
            
            leftCount,leftNode = rev(i+1)
            rightCount,rightNode = rev(i+1+leftCount)
            # print(i,data[i],data[i+1],data[i+1+leftCount])
            
            
            root.left = leftNode
            root.right = rightNode
            
            return (leftCount+rightCount+1,root)
        
        totalCount,root = rev(0)
        
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))