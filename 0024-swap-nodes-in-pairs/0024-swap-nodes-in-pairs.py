# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def swap(firstNode):
            if firstNode is None or firstNode.next is None:
                return firstNode
            
            secondNode,thirdNode = firstNode.next,firstNode.next.next 
            
            firstNode.next = swap(thirdNode)
            secondNode.next = firstNode 
            
            return secondNode
        
        return swap(head)
            