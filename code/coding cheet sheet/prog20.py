#count the occurance of an element in an array

def countOccurance(arr, ele):
    count=0
    for i in range(len(arr)):
        if arr[i]==ele:
            count+=1
    return count

print(countOccurance([5,2,1,4,2],2))