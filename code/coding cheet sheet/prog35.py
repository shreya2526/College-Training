def findCount(arr, length, num ,diff):
    count=0

    for i in range(length):
        subs=num-arr[i]
        if(abs(subs)<=2):
            count+=1
    return count if count>0 else -1

arr=[12,3,14,56,77,13]
print(findCount(arr,len(arr),13,2))
        