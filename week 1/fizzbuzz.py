def fizz_buzz(n):
    li = []
    for i in range(n):
        if i %3 == 0:
            li.append("fizz")
        if i %5 == 0:
            li.append("buzz")
        if i %3 == 0 and i%5==0:
            li.append("fizzbizz")
        else:
            li.append(i)
    return li