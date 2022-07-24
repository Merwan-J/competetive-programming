# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        x being duplicate 
        smaller head: stored
        larger head: stored
        
        collect the smaller elts
        collect the larger nodes
        connect the smalller tail to the larger head
        '''
        if head is None or head.next == None:
            return head
        
        larger = ListNode(101)
        smaller = ListNode(-101)
        returnNode = ListNode(-101)
        foundL = ListNode(101)
        
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
                
                if returnNode.val == -101:
                    returnNode.next =  smaller
                    returnNode  = returnNode.next
            else:
                larger.next = head
                larger = larger.next
                
                if foundL.val == 101:
                    foundL.next = larger
                    foundL = foundL.next
                
            head = head.next
            
        larger.next = None #this part is what killed my time
        if foundL.val == 101:
            foundL = None
            
        smaller.next = foundL
        if smaller.val == -101:
            returnNode = smaller.next
        
        return returnNode 

        
        
        
                    