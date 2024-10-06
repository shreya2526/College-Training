def missingNumber(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(0, n-1):
        xor2 ^= arr[i]
    
    for i in range(0, n):
        xor1 ^= i

    return xor1 ^ xor2

# arr = [3, 0, 1]
# n = 4
# print(missingNumber(arr, n))


def missing(arr, n):
    sum=(n)*(n+1)/2
    tot=0
    for i in range(0,len(arr)):
        tot+=arr[i]
    return int(sum-tot)

arr = [3, 0, 1]
n = len(arr)
print(missing(arr, n))
