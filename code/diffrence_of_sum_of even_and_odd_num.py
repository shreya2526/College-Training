import math


def difference(m,n):
    sq=0
    sum1, sum2=0,0
    for i in range(m,n):
        sq= math.sqrt(i)
        if(i%2==0):
            sum1+=sq
        else:
            sum2+=sq
    return int(sum1-sum2)

print(difference(1,10))
            