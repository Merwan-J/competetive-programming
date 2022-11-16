class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        rightMax = [n]*n
        leftMax = [-1]*n
        mod = 10**9 + 7
        
        stack = [-1]
        for i,num in enumerate(arr):
            while stack[-1]!=-1 and num<arr[stack[-1]]:
                rightMax[stack.pop()] = i
            leftMax[i] = stack[-1]
            stack.append(i)
        
        ans = 0
        for i,num in enumerate(arr):
            ans+= (i-leftMax[i])*(rightMax[i]-i)*num
            ans%=mod
        return ans
            
        
            
        