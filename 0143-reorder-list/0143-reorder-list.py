# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
         
        slow,fast = head,head 
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        
        cur = slow.next 
        slow.next = None 
        prev = None
        
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        
        
        head1,head2 = head,prev 
        
        while head2:
            head1Next = head1.next
            head2Next = head2.next 
            
            head1.next = head2
            head2.next = head1Next
            
            head1 = head1Next 
            head2 = head2Next 
        
        return head 
            
        
        
            