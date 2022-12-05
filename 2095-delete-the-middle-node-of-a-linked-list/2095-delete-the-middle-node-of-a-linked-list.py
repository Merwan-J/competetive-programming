# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         [1,2,3,4]
        
#         how to remove??
#         get to the middle element, connect the prev element and next element
        
#         three cases:
#             head: dummy-node
#             middle: using prev
#             tail: using prev

        dummy = ListNode(None,head)
        prev = dummy
        
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
            
        prev.next = slow.next
        return dummy.next
            