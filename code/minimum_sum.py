import math

def minSum(arr):
    arr.sort()
    add=0
    for i in range(len(arr)-1):
        add+=abs(arr[i]-arr[i+1])
    return add
arr=[1,3,2]
print(minSum(arr))