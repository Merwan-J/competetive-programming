class Solution:
    def spiralOrder(self, matrix):
#         result = []
#         column = []
#         def last_row(start,end):
#                 for i in matrix[-1][::-1][start:len(matrix[0])-end]:
#                     result.append(i)
#                 matrix.pop()

#         def first_row(start,end):
#                 for i in matrix[0][start:len(matrix[0])-end]:
#                     result.append(i)
#                 matrix.pop(0)

#         def first_column(start,end):
#                 for i in column[0][::-1][start:len(column[0])-end]:
#                     result.append(i)
#                 column.pop(0)

#         def last_column(start,end):
#                 for i in column[-1][start:len(column[0])-end]:
#                     result.append(i)
#                 column.pop()

#         for i in range(len(matrix[0])):
#             li = []    
#             for j in range(len(matrix)):
#                 li.append(matrix[j][i])
#             column.append(li)
#         if len(column)==1:
#             return column[0]
#         start = 0
#         end = 1

#         while len(matrix) and len(column):
#             if len(matrix) ==1:
#                 first_row(start,end-1)
#                 break
#             first_row(start,end)
#             if len(column)==1:
#                 last_column(start,end-1)
#                 break
#             last_column(start,end)
#             if len(matrix)==1:
#                 last_row(start,end-1)
#                 break
                
#             last_row(start,end)
#             first_column(start,end)
#             start +=1
#             end += 1
        
#         return result
#         left,right and bottom an top pointers
        l,r = 0,len(matrix[0])
        t,b = 0,len(matrix)
        result = []
        
        while l<r and t<b:
#             go through the first row
            for i in range(l,r):
                result.append(matrix[t][i])
            t+=1
#             then the last column
            for i in range(t,b):
                result.append(matrix[i][r-1])
            r-=1
            
#             check for the conditions again 
            if not(l<r and t<b):
                break
                
#                 go through the last row
            for i in range(r-1,l-1,-1):
                result.append(matrix[b-1][i])
            b-=1
#               go through the first column
            for i in range(b-1,t-1,-1):
                result.append(matrix[i][l])
            l+=1
        return result
            
        
