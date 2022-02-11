class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        arr = []
#         for i in range(m):
#             arr.append(nums1[i])
        
#         for j in range(n):
#             arr.append(nums2[j])
        
        
#         arr.sort()
        
        
            
        
        p1,p2 = 0,0
        
        while p1<m or p2<len(nums2):
            if p1<m and p2<len(nums2):
                if nums1[p1]>=nums2[p2]:
                    arr.append(nums2[p2])
                    p2+=1
                else:
                    arr.append(nums1[p1])
                    p1+=1
            elif p1<m:
                arr.append(nums1[p1])
                p1+=1
            else:
                arr.append(nums2[p2])
                p2+=1
        
        for i in range(len(arr)):
            nums1[i] = arr[i]
        
        