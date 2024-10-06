def isPrime(num):
    i=0
    if num<=1:
        return "not prime"
    if num==2:
        return "prime"
    for i in range (3, num*num):
        if num%i ==0:
            break
    if i<num:
        return "not prime"
    else:
        return "prime"


print(isPrime(109))