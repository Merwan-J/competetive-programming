class Solution:
    def maxArea(self, li: List[int]) -> int:
        l,max_area,r = 0,0,len(li)-1
        

        for i in li:
            max_area = max(max_area,min(li[l],li[r]) * (r-l))
            if li[r] < li[l]:
                r-=1
            else:
                l+=1

            if not l<r:
                break
                
        return max_area
