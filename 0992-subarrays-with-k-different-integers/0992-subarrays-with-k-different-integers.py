class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atmostK(k):
            l = 0
            count = 0
            hmap = {}
            
            for r in range(len(nums)):
                cur = nums[r]
                hmap[cur] = hmap.get(cur,0) + 1
                
                while len(hmap)>k and l<=r:
                    hmap[nums[l]] -= 1
                    if hmap[nums[l]] == 0: 
                        del hmap[nums[l]]
                    l+=1
                
                count += r-l+1
            
            return count 
        
        return atmostK(k)-atmostK(k-1)