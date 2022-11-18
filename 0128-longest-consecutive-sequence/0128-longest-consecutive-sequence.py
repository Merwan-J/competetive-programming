class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
#         consecutive elements -> increasing or decreasing subsequence of difference 1
        
#         thinking about using hashmap and hashset
        
#         hashmap: stores the length of previous consecutive elements
#         hashset: stores previously seen nums 
        
#         [100,4,200,1,3,2]
        
#         hmap                        hset
#         100:1                       100
#         4:
            
            
#         sorting would have made it easy: since it will group consecutive elts together 
#         but since we are told to write O(n) algorithm, need to find some other approach
        
#         what if we think of it as the longest subsequence that includes given num
        
#         for example [100,4,200,1,3,2]
        
#         the length subsequence that contains nums[i] = length of sub that contains nums[i]+1 and nums[i]-1
        
#         length(nums[i]) = len(nums[i] + 1) + len(nums[i]-1) + 1
        
        
#         100: look for 99 and look for 101, both are zero, 100 == 1
#         4: look for 3 and look for 5, both zero for now, 4 == 1
#         200: 201 and 199 both are zero for now, 200 == 1
#         1: 0 and 2 both are zero for now 1== 1
#         3: 4 and 2, 4==1 and 2 == 0 thus 3 == 2
#         2: 3 and 1, 3 == 2 and 1 == 1, thus 1 + 2 + 1  == 4
        
        
#         [0,3,7,2,5,8,4,6,0,1]
        
#         0:1
#         3:1
#         7:1
#         2:2
#         5:1
#             8:2
#             4:3
#             6:3
#             0
        n = len(nums)
        parent = [i for i in range(n)]
        size = [1]*n
        
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x,y):
            a = find(x)
            b = find(y)
            
            if size[a]<size[b]:
                a,b = b,a
            
            size[a]+=size[b]
            parent[b] = a
        
        seen = defaultdict()
        for i,num in enumerate(nums):
            if num not in seen and num - 1 in seen:
                union(i,seen[num-1])
            if num not in seen and num + 1 in seen:
                union(i,seen[num+1])
            if num not in seen:
                seen[num] = i
        
        return 0 if nums == [] else max(size)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        