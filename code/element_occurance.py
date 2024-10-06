#type1

def element_occurance(arr):
    occ={}
    for ele in arr:
        if ele in occ:
            occ[ele]+=1
        else:
            occ[ele]=1
    return occ

arr=[10,15,5,15,10]
occ=element_occurance(arr)
for key, value in occ.items():
    print('element: ' + str(key) + ' frequency: ' + str(value))

#type2

from collections import Counter

def count_occurrences(arr):
    return Counter(arr)