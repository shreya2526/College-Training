def element(arr, num):
    count=0
    for i in range(len(arr)):
        if arr[i]==num:
            count+=1
    
    return count

print(element([1,2,5,1,5,3], 5))