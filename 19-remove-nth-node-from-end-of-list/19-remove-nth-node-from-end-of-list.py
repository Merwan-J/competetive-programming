# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        arr = []
        while head:
            arr.append(head)
            head = head.next
        if len(arr) == n:
            return arr[1]
        
        arr[len(arr)-n-1].next = arr[len(arr)-n].next
        return arr[0]
        
        
                
        
        