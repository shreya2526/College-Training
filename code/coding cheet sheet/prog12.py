#number prime nums in given range
import math
def isPrime(num):
    prime=True
    if num==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(num))+1):
            if num%i==0:
                prime=False
                break

        if(prime):
            return True
        return False
    
def countPrime(n1,n2):
    count=0

    for i in range(n1,n2+1):
        if(isPrime(i)):
            count+=1

    return count

print(countPrime(11,17)) 