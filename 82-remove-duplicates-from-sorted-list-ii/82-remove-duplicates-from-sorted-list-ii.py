# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        headNode = head
        prev = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
                temp = head.next
                
                while temp and head.val == temp.val:
                    head.next = temp.next
                    temp = temp.next
                 
#               egde case handling
                if head==prev:
                    prev = head.next
                    headNode = prev
                    head = head.next
                    continue
                prev.next = head.next
                
            else:
                prev = head
                
            head = head.next
        return headNode
                
                
                
