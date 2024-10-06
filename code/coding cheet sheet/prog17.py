#find missing number in an array

#XOR

def missingNum(arr):
    n=len(arr)
    xor1,xor2=0,0
    for n1 in arr:
        xor1^=n1
    for i in range(1,n+1):
        xor2^=i
    return xor1^xor2

#sum of n natural numbers

def missingVal(arr):
    n=len(arr)
    add=(n*(n+1))//2
    ele_sum=sum(arr)
    return add-ele_sum

print(missingNum([3,0,1]))