# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firsthead = head
        
        count = 0
        while head.next:
            head = head.next
            count+=1
        
        middle = (count+1)//2
        count = 0
        head = firsthead
        while True:
            if middle == count:
                return head
            head = head.next
            count += 1
            