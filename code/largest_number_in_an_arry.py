def largeNumber(arr):
    num=arr[0]
    for i in range(len(arr)):
        if num<arr[i]:
            num=arr[i]
    return num
arr=[1,4,6,7,8,9]
print(largeNumber(arr))