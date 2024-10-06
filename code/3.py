def func(s,n):
    digit_count=[0]*10

    if s is None:
        return 0
    
    for i in range(0,n):
        digit_count[int(s[i])]+=1

    for i in range(0,n):
        if(int(s[i])!=digit_count[i]):
            return 0

    count=sum(1 for i in digit_count if i>0)
    
    if count>0:
        return count
    else:
        return 0