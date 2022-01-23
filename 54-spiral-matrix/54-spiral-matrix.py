class Solution:
    def spiralOrder(self, matrix):
        result = []
        column = []
        def last_row(start,end):
                for i in matrix[-1][::-1][start:len(matrix[0])-end]:
                    result.append(i)
                matrix.pop()

        def first_row(start,end):
                for i in matrix[0][start:len(matrix[0])-end]:
                    result.append(i)
                matrix.pop(0)

        def first_column(start,end):
                for i in column[0][::-1][start:len(column[0])-end]:
                    result.append(i)
                column.pop(0)

        def last_column(start,end):
                for i in column[-1][start:len(column[0])-end]:
                    result.append(i)
                column.pop()

        for i in range(len(matrix[0])):
            li = []    
            for j in range(len(matrix)):
                li.append(matrix[j][i])
            column.append(li)
        if len(column)==1:
            return column[0]
        start = 0
        end = 1
        while len(matrix) and len(column):
            if len(matrix) ==1:
                first_row(start,end-1)
                break
            first_row(start,end)
            if len(column)==1:
                last_column(start,end-1)
                break
            last_column(start,end)
            if len(matrix)==1:
                last_row(start,end-1)
                break
            last_row(start,end)
            # if len(column)==1:
            #     first_column(start,end-1)
            #     break
            first_column(start,end)
            start +=1
            end += 1
        
        return result