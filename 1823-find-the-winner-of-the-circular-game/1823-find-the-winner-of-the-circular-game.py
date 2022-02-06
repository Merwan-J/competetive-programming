class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = collections.deque(list(range(1,n+1)))
        
        def helper():
            if len(arr)==1:
                return arr[0]
            
            count=1
            
            while count<k:
                temp = arr.popleft()
                arr.append(temp)
                count+=1
            arr.popleft()
            
            return helper()
        
        return helper()