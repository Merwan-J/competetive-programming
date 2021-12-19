def bubble_sort(li):
    for i in range(len(li)):
        check = 0
        for j in range(len(li)):
            if j+1 < len(li) and li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                check +=1
    
        if check==0:
            return li
    

def insertion_sort(li):
    for i in range(1,len(li)):
        crnt_value = li[i]
        crnt_index = i
        for j in range(len(li)):
            compare_index = crnt_index - 1

            if crnt_value < li[compare_index]:
                li[crnt_index] = li[compare_index]
                li[compare_index] = crnt_value
                crnt_index -= 1
                compare_index -= 1

            if compare_index == -1 or crnt_value > li[compare_index]:
                break
    return li


def counting_sort(li):
    new_li = [0 * i for i in range(max(li)+1)]
    for i in set(li):
        count = li.count(i)
        new_li[i] = count

    an_li = []
    for j in range(len(new_li)):
        for k in range(new_li[j]):
            an_li.append(j)
    return an_li


def selection_sort(li):
    for i in range(len(li)):
        if i+1 == len(li):
            return li
        crnt_min = li[i]
        rest_min = min(li[i+1::])

        if rest_min < crnt_min:
            rest_index = li[i+1:].index(rest_min) + len(li[:i+1])
            li[i] = rest_min
            li[rest_index] = crnt_min
    return li
# print(bubble_sort([2,4,5,1,7,2,4,5,6,2,1,52,9,223,132,113,63623,112312]))
# # print(selection_sort([5,3,4,6,7,1,3]))

# print(selection_sort([2,4,5,1,7,2,4,5,6,2,1,52,9,223,132,113,63623,112312]))


def sortSentence(s: str) -> str:
    s = s.split(' ')
    li = []
    for i in range(len(s)):
        for j in s:
            print(str(i+1),j[-1])
            if str(i+1) == j[-1]:
                li.append(j[:len(j)-1])
                break
    return ' '.join(li)


# print(sortSentence("Myself2 Me1 I4 and3"))


def smallerNumbersThanCurrent(li):
    s = counting_sort(li)
    d = {}
    for i in set(s):
        d[i] = len(s[:s.index(i)])
    for i in range(len(li)):
        li[i] = d[li[i]]
    return li

# print(smallerNumbersThanCurrent([8,1,2,2,3]))
# [4,0,1,1,3]
# [6,5,4,8]
# Output: [2,1,0,3]

def kClosest(li,k):
     li = sorted(li,key=lambda x: x[0]**2 + x[1]**2)
     return li[:k]

# print(kClosest([[1,2],[1,0],[0,1],[5,6],[7,8]],4))

def arrange(li):
    print(li,'main')
    for i in range(len(li)):
        check = 0
        for j in range(len(li)-2):
            
            if li[j] == li[j+1] and li[j+1] != li[j+2]:
                li[j+1], li[j+2] = li[j+2], li[j+1]
                check +=1
            if li[j] != li[j+1] and li[j+1]==li[j+2]:
                li[j], li[j+1] = li[j+1], li[j]
                check +=1
            if j+3 < len(li) and li[j] == li[j+1] and li[j+1]== li[j+2] and li[j+2]!=li[j+3]:
                li[j+3],li[j+1] = li[j+1], li[j+3]

    return li
# print(arrange([1,1,1,1,2,2,3,3]))




def arrangeli(li):
    for i in range(len(li)):
        count = 0
        for j in range(len(li)-1):
            a = calculate_distance(li[j])
            b = calculate_distance(li[j+1])
            if a > b:
                li[j],li[j+1] = li[j+1], li[j]
                count += 1
        if count == 0:
            return li[:k]
    



class Solution:
    def largestNumber(self, li):
        print(li)
        li = [str(i) for i in li]
 
        for i in range(len(li)):
            count = 0
            for j in range(len(li)-1):
                a = int(li[j][0])
                b = int(li[j+1][0])
                print(a,b,"comparing",count)
                if a < b:
                    print('a is less than')
                    li[j], li[j+1] = li[j+1], li[j]
                    print(li,'after comparing')
                    count+=1
                if a == b:

                    num = int(''.join(li))
                    li[j], li[j+1] = li[j+1], li[j]
                    num2 = int(''.join(li))
                    if num > num2:
                        li[j], li[j+1] = li[j+1], li[j]

            if count ==0:
                return ''.join(li)
# print(int('1'[1:]))
# sol = Solution()




def largest_number(li):
    li = [str(i) for i in li]
    for i in range(len(li)):
        count =0 
        for j in range(len(li)-1):
            num = int(''.join(li))
            li[j], li[j+1] = li[j+1], li[j]
            num2 = int(''.join(li))
            if num > num2:
                li[j], li[j+1] = li[j+1], li[j]
                count+=1
        if count==0:
            return ''.join(li)



def rearrangeArray(li):
    for i in range(len(li)):
        count = 0
        for j in range(1,len(li)-1):
            l = li[j-1]
            r = li[j+1]
            a = (l+r)/2
            print(l,r,a,li[i])
            if li[j] == a:
                li[j-1],li[j] = li[j],li[j-1]
                print(li)
                count+=1
    return li

# print(rearrangeArray([0,3,2,4,17,1,11,18,13]))


def rearrangeArray(li):
    for i in range(1,len(li)-1):
        crnt_value = li[i]
        crnt_index = i
        for j in range(len(li)):
            l = crnt_index - 1
            r = crnt_index + 1
            a = (l+r)/2
            if crnt_value == a:
                li[crnt_index] = li[crnt_index-1]
                li[crnt_index-1] = crnt_value
                crnt_index -= 1
                

            if crnt_index == -1:
                break
    return li


class Solution:
    def findOriginalArray(self, li):
        multiples = []
        factors = []
        for i in li:
            for j in range(len(li)):
                if i*2 == li[j]:
                    multiples.append(i)
                if i/2 == li[j]:
                    factors.append(i)
            # if len(list(set(multiples) - set(factors))) == len(li)//2:
            #     return multiples
        return multiples,factors,set(multiples)-set(factors)

# sol = Solution()
# print(sol.findOriginalArray([1,2,4,3,6,8]))
# check backwards and forward
# check forward if is multiple exist 
# check backward if its factor exists

li = [1,2,4,3,6,8]
def find_original(li):
    li = sorted(li)
    n = li[::]
    l = len(li)
    for i in range(len(li)):
        count = 0
        for j in range(len(li)):
            if j< len(li) and i<len(li):
                if li[i]*2 == li[j]:
                    li.remove(li[j])
                    continue
                else:
                    count+=1 
            if count == len(li):
                li.remove(li[i])
            if len(li) == l/2:
                return li
            elif j> len(li) and i>len(li):
                return []
# print(find_original(li))


class Solution:
    def findOriginalArray(self, li):
        li = sorted(li)
        n = li[::]
        new_li = []
        for i in n:
            for j in n:
                if i*2 == j:
                    new_li.append(i)
                    n.remove(j)
                    n.remove(i)
             
        return []
        
    


def original(li):
    li = sorted(li)
    d = {}
    new_li = []

    for i in li:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    for key in li:
        if key!=0 and key*2 in d and d[key]==1 and d[key*2]== 1:
            new_li.append(key)
            d[key] -= 1
            d[key*2] -= 1
        if key ==0 and d[key]>=2:
            new_li.append(key)
            d[key] -= 2
        if len(new_li) == len(li)/2:
            return new_li

    return []


def frequency(li,k):
    li = sorted(li)
    n = k
    d = {'num':1}
    count = 1
    index = len(li)-1
    i = len(li)-1
    max = li[index]
    while i >= 0:
        if i == 0:
            return d
        i -= 1
        
        if max - li[i] <= n:
            n = n- (max -li[i])
            count += 1
            if count > d['num']:
                d['num'] = count
                
        else:
            n = k
            count = 1
            index -= 1
            max = li[index]
            i = index 


# print(sorted(li))


# print(len(li),len(list(set(li))))
# sum = 0
# for i in set(li):
#     sum += 10000-i
# print(sum)

def frequency(li,k):
    li = sorted(li)
    start,end,sum  = 0,0,0
    count = 1
    for i in range(len(li)):
        sum += li[end]
        length = end-start + 1
        if length*li[end] - sum <= k:
            if length > count:
                count += 1
        else:
            sum -= li[start]
            start += 1
        end +=1
    return count
            
# print(frequency([1,2,8,13],5))
# li = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
# k = 3056
# # li = [1,2,4]
# # k = 5
# # li = [3,9,6]
# # k = 2
# print(frequency(li,k))


# def arthmeticarray(li,l,r):
#     start = 0
#     end = 1
#     diff = ''
#     sub_lis = []
#     bool_list = []
#     for i in range(len(li)):
#         sub_li = li[l[i]:r[i]+1].sort()
#         sub_lis.append(sub_li)
    
#     for i in sub_lis:
#         for j in range(len(i)):
#             new_dif = i[end] - i[start]
#             if diff == '':
#                 diff = new_dif
#             else:
#                 if new_dif == diff:
#                     start += 1
#                     end += 1
#                 else:
#                     bool_list.append("false")
#                     break
#             if end == len(i):
#                 start = 0
#                 end = 1
#                 break
            

# def artArr(li,l,r):
#     start = 0
#     end = 1
#     sub_lists = []
#     bool_list = []
#     diff = ''

#     for i in range(len(l)):
#         sub_li = li[l[i]:r[i]+1]
#         sub_lists.append(sorted(sub_li))
#     print(sub_lists,"the lists")
#     for i in sub_lists:
#         print(i,"#############################")
#         for j in range(len(li)):
#             if end == len(i):
#                 start = 0
#                 end = 1
#                 diff = ''
#                 bool_list.append("true")
#                 break

#             new_diff = i[end] - i[start]
#             print(diff,new_diff,"the differences",i[end],i[start])
#             if diff == '':
#                 print("added the diff")
#                 diff = new_diff
#                 start += 1
#                 end += 1
#             elif diff != '':
#                 if new_diff == diff:
#                     print("they are equal")
#                     start += 1
#                     end += 1
#                 elif new_diff != diff:
#                     start = 0
#                     end = 1
#                     diff = ''
#                     bool_list.append("false")
#                     break
#     return bool_list           


def artArr(li,l,r):
    bool_li = []
    for i in range(len(l)):
        sub_li = sorted(li[l[i]:r[i]+1])
        print(sub_li)
        diff = sub_li[1]- sub_li[0]
        count = 0
        for j in range(len(sub_li)-1):
            new_diff = sub_li[j+1] - sub_li[j]
            print(sub_li[j+1],sub_li[j])
            if new_diff != diff:
                count += 1
        if count == 0:
            bool_li.append("true")
        else:
            bool_li.append("false")

    return bool_li




# print(artArr([4,6,5,9,3,7],[0,0,2],[2,3,5]))



def max_coins(li):
    li = sorted(li)
    l = len(li)//3
    li = li[l:]
    sum = 0

    for i in range(0,len(li),2):
        sum += li[i]
    return sum
# print(max_coins([9,8,7,6,5,1,2,3,4]))



def reduce_arr(li):
    d = dict()
    for i in li:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    count =1
    sum = 0
    n = len(li)/2
    for key,value in d.items():
        sum+= value
        print(sum)
        if sum>= n:
            return count
        count+=1

# print(reduce_arr([5,3,3,3,3,5,5,2,2,7]))
    


import random
def pancake_sort(li):
    copy_li = sorted(li)
    is_sorted = False
    nums = []

    start,end = 0,1
    while not is_sorted:
        if end == len(li):
            break
        print(li[start],li[end],"the variables")
        if li[start] > li[end]:
            # swap
            sub_li = li[:end+1][::-1]
            print(sub_li,"sub_li")
            rest = li[end+1:]
            li = [*sub_li,*rest]
            nums.append(end+1)
            # add end+1 to the list
        if copy_li == li:
            return nums
        start += 1
        end += 1
        # increment start,end
        # compare it to the sorted list


# print(pancake_sort([3,2,4,1]))


# dictionary 
# pointer [start,end]
# check if the next elt is opening or closing
# if opening use pointers
# if closing check for match
#  poping 

def calculate(left,right,i):
    if i == '+':
        total = left + right
    elif i == '*':
        total = left * right
    elif i == '-':
        total = left - right
    else:
        total = int(left / right)
    print(left,right,i,"calculated")
    return total

def eval(li):
    d = '/*-+'
    stack = []
    for i in li:
        if i in d:
            total = calculate(stack[-2],stack[-1],i)
            stack = stack[:-2]
            stack.append(total)
        else:
            stack.append(int(i))
    return stack[0]

   
# print(eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))



def reverseParentheses(s):
    op = '()'
    stack = []
    output = ''

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            sub_s = s[stack[-1]+1:i][::-1]
            b_rest_s = s[:stack[-1]+1]
            t_rest_s = s[i:]
            s = b_rest_s+sub_s+t_rest_s
            stack = stack[:-1]
    for i in s:
        if i not in op:
            output+=i

    return output


# reverseParentheses("(u(love)i)")
