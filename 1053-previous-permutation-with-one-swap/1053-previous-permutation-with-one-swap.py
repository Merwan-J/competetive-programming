class Solution:
    def prevPermOpt1(self,arr):
        if len(arr) <= 1:
            return arr

        idx = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                idx = i - 1
                break

        if idx == -1:
            return arr

        for i in range(len(arr) - 1, idx, -1):
            if arr[i] < arr[idx] and arr[i] != arr[i - 1]:
                arr[i], arr[idx] = arr[idx], arr[i]
                break

        return arr



