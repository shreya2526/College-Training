def max_length(arr):
    arr=[-1 if x==0 else 1 for x in arr]

    sum_map={}
    max_len=0
    cum_sum=0
    
    sum_map[0]=-1

    for i in range(len(arr)):
        cum_sum+=arr[i]

        if cum_sum in sum_map:
            length=i-sum_map[cum_sum]
            max_len=max(max_len,length)
        else:
            sum_map[cum_sum]=i
    
    return max_len
arr=[1,0,1,1,1,0,0]
print(max_length(arr))