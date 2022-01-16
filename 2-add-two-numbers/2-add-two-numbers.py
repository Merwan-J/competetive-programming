# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        
        while l1 or l2 :
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val)
                l2 = l2.next
        
        ans = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        
        nodes = []
        
        for digit in ans:
            node = ListNode(int(digit))
            nodes.append(node)
        
        for _index in range(len(nodes)-1):
            nodes[_index].next = nodes[_index+1]
        
        return nodes[0]