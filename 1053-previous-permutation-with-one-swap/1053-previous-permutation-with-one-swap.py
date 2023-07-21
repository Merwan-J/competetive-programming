class Solution:
    def prevPermOpt1(self,arr):
        if len(arr) <= 1:
            return arr

        for j in range(len(arr) - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                break

        if j == -1:
            return arr

        for i in range(len(arr) - 1, j, -1):
            if arr[i] < arr[j] and arr[i] != arr[i - 1]:
                arr[i], arr[j] = arr[j], arr[i]
                break

        return arr



