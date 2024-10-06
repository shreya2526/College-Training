def checkSuperior(arr, n):
    count=1
    max_right=arr[-1]

    for i in range(n-2, -1, -1):
        if(arr[i]>max_right):
            count+=1
            max_right=arr[i]
    
    return count
arr=[8,10,6,2,9,7]
print(checkSuperior(arr, len(arr)))