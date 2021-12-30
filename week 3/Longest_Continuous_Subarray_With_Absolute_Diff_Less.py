class Solution:
    def longestSubarray(self, li: List[int], limit: int) -> int:
        l,r = 0,0
        mx = li[0]
        mn = li[0]
        count = 0

        while True:
            # print(li[l:r+1])
            if mx-mn <= limit:
                count = max(count,r-l+1)
                r+=1
                
                if r==len(li):
                    return count

                if li[r] < mn:
                    mn = li[r]
                if li[r] > mx:
                    mx = li[r]
            else:
                l+=1
                r+=1
                
                if r ==len(li):
                    return count
                    
                if li[l-1] == mn:
                    mn = min(li[l:r+1])
                elif li[l-1] == mx:
                    mx = max(li[l:r+1])
                
                if li[r] < mn:
                    mn = li[r]
                if li[r] > mx:
                    mx = li[r]
                
