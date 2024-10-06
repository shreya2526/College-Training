#the number of the files is according to the questions of prepinsta playlist.

def func(n):
    array=[]
    evenArr=[]
    oddArr=[]
    
    for i in range(0,n):
        number=int(input('Enter the input in array: '))
        array.append(number)

    for i in range(0,n):
        if(i%2==0):
            evenArr.append(array[i])
        else:
            oddArr.append(array[i])

    sorted(evenArr)
    sorted(oddArr)

    sum=evenArr[-2]+oddArr[-2]

    return sum