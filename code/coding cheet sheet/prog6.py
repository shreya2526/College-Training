#minimum steps stairs 

def minSteps(n,m):
    count_m=n//m
    rem_dist=n%m

    if rem_dist>0:
        count_m+=1

    return count_m

print(minSteps(5,2))