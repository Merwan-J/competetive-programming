# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        headNode = head  
        while head and head.next:
            print(head.val)
            if head.val == head.next.val:
                head.next = head.next.next
                temp = head.next
                while temp and temp.val == head.val:
                    temp = temp.next
                    head.next = head.next.next
            head = head.next
        return headNode