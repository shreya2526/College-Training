#difference of sum of square roots of odd and even numbers in a range
import math
def difference(m,n):
    odd_sum,eve_sum=0,0
    for i in range(m,n+1):
        if i%2==0:
            eve_sum+=math.sqrt(i)
        else:
            odd_sum+=math.sqrt(i)
    return abs(eve_sum-odd_sum)

print(difference(1,10)) 