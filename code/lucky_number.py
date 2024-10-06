def chooseLuckyNumber(num):
    luckyNumbers=[4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    n=len(luckyNumbers)//len(str(luckyNumbers[0]))
    for i in range(0,n):
        if(num%luckyNumbers[i]==0):
            return True
    return False

print(chooseLuckyNumber(467))