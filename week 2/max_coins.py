def max_coins(li):
    li = sorted(li)
    l = len(li)//3
    li = li[l:]
    sum = 0

    for i in range(0,len(li),2):
        sum += li[i]
    return sum
