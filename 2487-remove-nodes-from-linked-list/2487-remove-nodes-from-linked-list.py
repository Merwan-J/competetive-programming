# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [] 
        
        while head:
            while stack and stack[-1]<head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next
        
        right = None
        
        for i in range(len(stack)-1,-1,-1):
            num = stack[i]
            cur = ListNode(num)
            cur.next = right 
            right = cur 
        
        return right 
            