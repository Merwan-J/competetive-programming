import math

nums = input().split(' ')

[m,n,a] = [ int(i) for i in nums]


square_area = m * n
flagstone_area = a**2

up = math.ceil(m/a)
side = math.ceil(n/a)

print(up * side)