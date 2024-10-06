#search in a 2d matrix

def checkTarget(arr, target):
    n=len(arr)
    m=len(arr[0])

    for i in range(n):
        if arr[i][0]<=target<=arr[i][n-1]:
            return binarySearch(arr[i],target)
    
        
def binarySearch(nums, target):
    n=len(nums)
    low,high=0,n-1

    while low<=high:
        mid=(low+high)//2

        if target==nums[mid]:
            return True
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    return False

arr=[[3,4,7,9],
     [12,13,16,18],
     [20,21,24,29]
    ]
print(checkTarget(arr,23))