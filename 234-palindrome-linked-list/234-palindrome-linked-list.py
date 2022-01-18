# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         This one takes O(N) Time and O(N) Space

#         arr = []
        
#         while head:
#             arr.append(head.val)
#             head = head.next
        
#         return arr==arr[::-1] 

# But this code takes O(N) time and O(1) space
# it first checks for the mid point 
# then reverse the second half of the list
# compares it to the first half of unreversed list
# if they are compliment it means the list is palindrome 
        fast,slow = head,head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        frontNode = None
        nextNode = slow
        
        while nextNode:
            _Next = nextNode.next
            nextNode.next = frontNode
            frontNode = nextNode
            nextNode = _Next
        
        while frontNode:
            if frontNode.val != head.val:
                return False
            frontNode = frontNode.next
            head = head.next
        return True