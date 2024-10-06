#max piece of cake

def maxNumberPieces(num):
    mod=1000000007
    pieces=(num*(num+1))//2+1
    return pieces%mod

print(maxNumberPieces(34))