def calculateMeta(num):
    count=0
    for i in range(1, num+1):
        if(i%2==0 and i%4==0 and i%8==0 and i%10!=0):
            count+=1
    return count

print(calculateMeta(13))