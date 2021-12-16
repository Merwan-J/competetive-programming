class Solution:
    def maxOperations(self, li,k):
        li.sort()
        count = 0
        d = {}
        for i in li:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in li:
            if i > k:
                return count
            dif = k-i
            if dif in d:
                if dif == i and d[dif] >= 2:
                    d[dif] -= 2
                    count += 1
                if dif != i and d[dif] > 0 and d[i] > 0:
                    d[dif] -= 1
                    d[i] -= 1
                    count += 1
        return count


# class Solution:
#     def maxOperations(self, li,k):
#         li.sort()
#         count = 0
#         d = {}
#         for i in li:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] += 1
#         for i in li:
#             print(d)
#             dif = k-i
#             if dif in d and d[dif] >0:
#                 if i == k/2:
#                     d[dif] -= 2
#                 else:
#                     d[dif] -= 1
#                 count += 1
 
            
#         return count
        

    

sol = Solution()
li = [1,2,3,4]
k = 5
li = [3,1,3,4,3,7,9,10]
k = 6
print(sol.maxOperations(li,k))

    

sol = Solution()
li = [1,2,3,4]
k = 5

print(sol.maxOperations(li,k))