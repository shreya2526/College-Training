#fibonacci series

n=int(input('enter range: '))
n1,n2=-1,1
fib=0
for i in range(n):
    fib=n1+n2
    print(fib,end=' ')
    n1=n2
    n2=fib