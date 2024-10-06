def findLargest(arr):
    mini=arr[0]

    for i in range(len(arr)):
        if arr[i]>mini:
            mini=arr[i]
    return mini

print(findLargest([1,2,3,4,5,10,4,5,6]))