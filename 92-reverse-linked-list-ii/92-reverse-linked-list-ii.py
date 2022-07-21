# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        """
        prev - this case 1
        node at left
        reverse them until 4
        next elments must be stored
        at the end: if prev,prev.next = head
                    node at left.next = next
        """
        
        prev = None
        headNode = head
        
        while head:
            if l == 1:
                leftNode = head
                p = None
                while head and r>0:
                    cur = head
                    head = head.next
                    cur.next = p
                    p = cur
                    r-=1
                leftNode.next = head
                if prev: prev.next = p
                return headNode if leftNode!=headNode else p
            prev = head
            head = head.next
            l-=1
            r-=1