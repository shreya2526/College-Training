#5-13 questions are to predict output

a=6
b=84

while(b>0):
    b=b/2
    a=a+6
    c=a+b
    while(c>40):
        if(c%2==0):
            print(a,' ')
        else:
            print(b,' ')
        c/=10
print(c)