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
        arr = []
        
        while head:
            arr.append(head)
            head = head.next
        
        l,r = 0, len(arr)-1
        
        while l<r:
            temp = arr[l].next
            arr[l].next = arr[r]
            arr[r].next = temp
            l+=1
            r-=1
            if not(l<r):
                temp.next = None
        
        return arr[0]