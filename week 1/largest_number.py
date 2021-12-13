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