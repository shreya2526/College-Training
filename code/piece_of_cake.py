def countPieceOfCake(n):
    mod=100000007
    sum=(n*(n+1))/2
    ans=sum+1
    return int(ans%mod)

print(countPieceOfCake(4))