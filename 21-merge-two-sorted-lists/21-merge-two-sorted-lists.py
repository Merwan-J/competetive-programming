# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2==None:
            ans = list1 if list1!=None else list2
            return ans
        
        prev = None
        headNode = list1 if list2.val>=list1.val else list2
        p1 = list1
        p2 = list2
        
        while p1 or p2:
            if p1 and p2:
                if p1.val>p2.val:
                    if prev:
                        prev.next = p2
                    prev = p2
                    p2 = p2.next

                else:
                    if prev:
                        prev.next = p1
                    prev = p1
                    p1 = p1.next
            else:
                prev.next = p1 if p1 else p2
                break

        return headNode
        
            