def fun(s, n):
    if n<4:
        return 0

    if s[0].isdigit():
        return 0
    
    cap=0
    num=0

    for i in range(0,n):
        if(s[i]==' ' or s[i]=='/'):
            return 0
        if(s[i]>='A' and s[i]<='Z'):
            cap+=1
        elif(s[i].isdigit()):
            num+=1

    if(cap>0 and num>0):
        return 1
    else:
        return 0