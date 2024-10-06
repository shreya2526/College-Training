def arrangeElement(arr):
    j,k=0,0
    pos=[]
    neg=[]

    for i in arr:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)

    ans=[]

    while j<len(pos) and k<len(neg):
        ans.append(pos[j])
        ans.append(neg[k])
        j+=1
        k+=1
    
    ans.extend(pos[j:])
    ans.extend(neg[k:])

    return ans

arr=[3,1,-2,5,2,-4]
print(arrangeElement(arr))
