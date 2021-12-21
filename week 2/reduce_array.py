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
