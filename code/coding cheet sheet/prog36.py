def findProductPair(arr,add):
    if arr is None or len(arr)<2:
        return -1
    
    smallest=arr[0]
    secSmallest=-99999999

    for i in arr:
        if smallest>i:
            secSmallest=smallest
            smallest=i
        elif i>smallest and i<secSmallest:
            secSmallest=i

    return smallest*secSmallest if (smallest+secSmallest<=add) else 0

arr=[5,2,4,3,9,7,1]
print(findProductPair(arr,9))