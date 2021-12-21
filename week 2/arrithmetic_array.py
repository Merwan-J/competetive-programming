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
            bool_li.append(True")
        else:
            bool_li.append(False)

    return bool_li
