# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
#        [ 1,  2,  3,  4]
#          ^a  ^b

        prev = None
        daHead = head.next
        
        while head and head.next:
            a = head
            b = head.next
            
            a.next = b.next
            b.next = a
            
            if prev:
                prev.next = b
                
            prev = a
            
            head = a.next
        
        return daHead
            
            
        