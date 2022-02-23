import heapq
n = int(input())
arr = []
deleted = dict()
heapq.heapify(arr)

for i in range(n):
    q = list(map(int,input().split()))
    if q[0]==3:
        while deleted[arr[0]]==0:
            heapq.heappop(arr)
        print(arr[0])
    elif q[0]==1:
        deleted[q[1]] = 1
        heapq.heappush(arr,q[1])
    elif q[0]==2:
        deleted[q[1]]=0
