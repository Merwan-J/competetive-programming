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