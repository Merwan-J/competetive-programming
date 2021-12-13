def grade(n):
    i = 5 - n%5
    if n<38:
        return n
    if i<3:
        return i+n

    return n


while True:
    num = int(input("enter: "))
    print(grade(num))
    break;