def countingValleys(steps, path):
    path = [i for i in 'UDDDUDUU']
    valley = 0
    track = 0
    li = []

    for i in path:
        if i == 'U':
            track +=1
            li.append('U')
            print(track,'it is up',li)
        if i == 'D':
            track -=1
            li.append('D')
            print(track,"it is down",li)
        if track == 0:
            print(li)
            if li[0] == 'D' and li[-1] == 'U':
                valley +=1
                print(track,valley,li)
            li = []
    return valley