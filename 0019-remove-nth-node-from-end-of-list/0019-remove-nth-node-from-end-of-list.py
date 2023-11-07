# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        total = 0
        cur = head 
        while cur:
            cur = cur.next
            total+=1 
        
        
        count = 1 
        dummy = ListNode(0,head)
        prev = dummy 
        cur = head 
        
        while count!=total-n+1:
            prev = cur
            cur = cur.next
            count+=1 
        
        prev.next = cur.next
        return dummy.next