def ratFood(arr,n, r, unit):
    if arr is None:
        return -1
    
    food=r*unit
    add=0

    for i in range(n):
        add+=arr[i]
        if(add>=food):
            return i+1
        
    return 0

arr=[2,8,3,5,7,4,1,2]
unit=2
r=7
n=len(arr)
print(ratFood(arr,n,r,unit))