import math
def calculate_distance(self,li):
    return math.sqrt(li[0]**2 + li[1]**2)
    
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