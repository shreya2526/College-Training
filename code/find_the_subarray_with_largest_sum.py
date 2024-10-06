def LargeSum(arr):
    sum=0
    maxi=0
    for i in range(len(arr)):
        sum+=arr[i]
        maxi=max(maxi,sum)
        if(sum<0):
            sum=0
    return maxi


arr=[-2,1,-3,4,-1,2,1,-5,4]
print(LargeSum(arr))