

def movenegetive(num):
    n=len(num)
    i=0
    j=0
    while i<n:
        if num[i] <0:
            num[i],num[j]=num[j],num[i]
            j=j+1
        i=i+1
    return num 




print(movenegetive([-1, 2, -3, 4, -5]))