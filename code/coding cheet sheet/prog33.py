def function(str1):
    if(str1 is None or len(str1) ==0):
        return -1
    
    ans=int(str1[0])

    for i in range(1,len(str1), 2):
        if str1[i]=='A':
            ans&=int(str1[i+1])
        elif str1[i]=='B':
            ans|=int(str1[i+1])
        elif str1[i]=='C':
            ans^=int(str1[i+1])
    
    return ans

str1="1C0C1C1C1A0B1"
print(function(str1))