# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None or head.next==None:
            return head
   
        crntnode = head
        frontnode = None
        nextnode = head
        
        while nextnode:
            # if crntnode == nextnode.val:
            #     nextnode = crntnode.next
            #     crntnode.next = None
            #     frontnode = crntnode
            crntnode = nextnode
            nextnode = crntnode.next
            crntnode.next = frontnode
            frontnode = crntnode
        return frontnode

            