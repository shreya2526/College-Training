#find the target elemet in an array

def findTarget(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
        
    return -1

print(findTarget([2,3,4,10,40],20))