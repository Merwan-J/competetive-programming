# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseGroup(node,k):
            cur = node
            prev = None 
            
            while k>0:
                nextt = cur.next 
                cur.next = prev
                prev = cur 
                cur = nextt 
                k-=1 
            
            return prev
        
        
        group = 1 
        count = 0 
        cur = head 
        prev = ListNode()
        
        
        while cur:
            # print(cur.val)
            size = 0 
            start = cur
            curPrev = prev
            while cur and size + count < (group*(group+1)/2):
                size+=1
                curPrev = cur
                cur = cur.next 
            
            if size%2 == 0:
                revStart = reverseGroup(start,size)
                prev.next = revStart
                prev = start 
            else:
                prev.next = start
                prev = curPrev 
            
            group+=1
            count+=size
            
        return head
                
             
        
        
        
                
        
                
            
        
        