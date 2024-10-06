def isFound(arr, num):
    for i in range(0,len(arr)):
        if arr[i]==num:
            return i
        
    return -1
        
arr=[2,3,4,10,40]
num=40
print(isFound(arr, num))

# type 2: using binary search

# def isFound(arr, num):
#     left=0
#     right=len(arr)-1
#     while(left<=right):
#         mid=int(left+(right-left)/2)

#         if arr[mid]==num:
#             return mid
#         if arr[mid]<num:
#             left=mid+1
#         else:
#             right=mid-1

#     return -1

# arr=[2,3,4,10,40]
# num=30
# print(isFound(arr, num))