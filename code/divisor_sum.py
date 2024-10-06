def divSum(num):
    add=0
    for i in range(1,num+1):
        if num%i==0:
            add+=i
    return add
print(divSum(48))