# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodeVals = []
        stack = []
        counterDict = dict()
        
        index = 0
        while head:
            nodeVals.append(head.val)
            counterDict[index] = 0
            head = head.next
            index += 1
        
        for i in range(len(nodeVals)):
            while len(stack) and nodeVals[i] > stack[-1][1]:
                if counterDict[stack[-1][0]] == 0:
                    counterDict[stack[-1][0]] = nodeVals[i]
                stack.pop()
            stack.append((i,nodeVals[i]))
        
        nodeVals = []
        for val in counterDict.values():
            nodeVals.append(val) 
        
        return nodeVals
        