class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        
        tickets = [(tickets[i],i) for i in range(len(tickets))]
        q = deque(tickets)
        total = 0
        
        while q:
            ticket,i = q.popleft()
            ticket-=1
            total+=1
            
            if ticket == 0 and i==k:
                return total
            
            if ticket:
                q.append((ticket,i))
        
        
            
        
        
        
        
        
    
    
