def func(num,m):
    if num%m==0:
        return num
    
    lower=(num//m)*m
    upper=lower+m

    if (num-lower)< (upper-num):
        return lower
    return upper

print(func(25,3))