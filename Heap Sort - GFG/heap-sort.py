
class Solution:
    def getParent(self,arr,i):
        return (i-1)//2

    def getRight(self,arr,i):
        return i*2 + 2

    def getLeft(self,arr,i):
        return i*2 + 1
    
    def getMin(self,arr):
        return arr[0]
    
    def swap(self,arr,left,right):
        arr[left],arr[right] = arr[right],arr[left]
    
    def change(self,arr,n):
        for i in range(n):
            arr[i]*=-1
        
    def upheap(self,arr,i):
        parent = self.getParent(arr,i)

        while i>0 and arr[i]<arr[parent]:
            self.swap(arr,i,parent)
            i = parent 
            parent = self.getParent(arr,i)

    def downheap(self,arr,n,i):
        
        while True:
            left = self.getLeft(arr,i)
            right = self.getRight(arr,i)
            swap = i

            if left < n and arr[left] < arr[i]:
                swap = left

            if right < n and arr[right] < arr[swap]:
                swap = right

            if swap == i:
                break 
            
            self.swap(arr,swap,i)
            i = swap 
           

    def insert(self,arr,elt):
        arr.append(elt)
        i = len(arr)-1
        self.upheap(arr,i)
        

    def heapify(self,arr,n,i):
        self.downheap(arr,n,i)

        
    def remove(self,arr,i,n):
        self.swap(arr,n,i)
        self.heapify(arr,n,i)

    def update(self,arr,i,num):
        arr[i] = num 
        self.heapify(arr,len(arr),i)
    
    def buildHeap(self,arr,n):
        for i in range(len(arr)):
            self.upheap(arr,i)
        
    def HeapSort(self,arr,n):
        r = n
        self.change(arr,n)
        self.buildHeap(arr,n)
        while r>0:
            r-=1
            self.remove(arr,0,r)
        self.change(arr,n)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends