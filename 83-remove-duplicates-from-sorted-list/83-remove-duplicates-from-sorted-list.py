# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headNode = ListNode(0,head)
        
        while head and head.next:
            temp = head.next
            while temp and head.val == temp.val:
                head.next = temp.next
                temp = temp.next
            head = head.next
        
        return headNode.next