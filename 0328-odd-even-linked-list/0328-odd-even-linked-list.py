# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        oddHead = ListNode(None,head)
        evenHead = ListNode(None,head.next)
        
#         oddHead
#         oddTail
#         evenHead
        
#         oddHead->oddTail->evenHead
        
#         I need to update( thier next values each time)
        
#         would there be a node at the last or at some position that won't be updated??
        
        
        prevEven = evenHead.next
        prevOdd = oddHead.next
        node = evenHead.next.next
        count = 3
        
        while node:
            if count%2:
                prevOdd.next = node
                prevOdd = node
            else:
                prevEven.next = node
                prevEven = node
            
            node = node.next
            count+=1
        
        prevEven.next = None
        prevOdd.next = evenHead.next
        
        return oddHead.next
        
        