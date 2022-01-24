# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        total = 0
        arr = []
        
        while head:
            arr.append(head)
            head = head.next
        
        i = 0
        n = len(arr)
        while i<=(n/2)-1:
            total = max(total,arr[i].val + arr[n-1-i].val)
            i+=1
        
        return total