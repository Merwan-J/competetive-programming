# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        headNode = prev = ListNode(0,head)
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
                continue
            prev = prev.next
            head = head.next
            
        return headNode.next