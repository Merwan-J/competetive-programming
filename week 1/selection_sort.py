#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
          print(*selectionSort(self,arr))
    
    def selectionSort(self, li,n):
        #code here
        for i in range(len(li)):
            if i+1 == len(li):
                return li
            crnt_min = li[i]
            rest_min = min(li[i+1::])

            if rest_min < crnt_min:
                rest_index = li[i+1:].index(rest_min) + len(li[:i+1])
                li[i] = rest_min
                li[rest_index] = crnt_min
        return li

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
