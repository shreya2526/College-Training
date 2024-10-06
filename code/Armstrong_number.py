def findArmStrongNumber(num):
    add=0
    n=num
    while(n>0):
        n1=n%10
        add+=n1**3
        n//=10
    if add==num:
        return True
    return False
print(findArmStrongNumber(2))