# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        
        while head:
            arr.append(head)
            head = head.next 
        
        arr = sorted(arr,key=lambda node: node.val)
        
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i].next = None
                break
            arr[i].next = arr[i+1]
        
        return arr[0]