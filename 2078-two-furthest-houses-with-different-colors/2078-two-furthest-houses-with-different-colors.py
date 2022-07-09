class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        right = n-1
        left = 0
        
        while colors[left]==colors[-1]:
            left += 1
        
        while colors[right] == colors[0]:
            right -= 1
        
        return max(n-left-1,right)
        