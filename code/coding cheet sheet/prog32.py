import math

def func(num):
    if 0<=num<=9:
        return num
    elif num%2!=0:
        return math.floor((num-2)//2)
    return math.floor(num/2)

print(func(37))