class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        result = []
        revArray = []
        
        while head:
            revArray.append(head)
            _Next = head.next
            if head.next==None and len(revArray) != k:
                result[-1].next = revArray[0]
                
            if len(revArray)==k:
                
                for i in range(len(revArray)-1,-1,-1):   
                    if i==0:
                        revArray[i].next = None
                        result.append(revArray[i])
                        continue  
                        
                    revArray[i].next = revArray[i-1]
                    
                    if i==len(revArray)-1 and len(result):
                        result[-1].next = revArray[-1]
                    result.append(revArray[i])
                    
                revArray = []
                
            head = _Next
        
        return result[0]
            