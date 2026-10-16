def leftrotate(num,k):
    k=k%len(num)
    i=0
    j=k-1
    while i <j:
        num[i],num[j]=num[j],num[i]
        i=i+1
        j=j-1
    i=k
    j=len(num)-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        j=j-1
        i=i+1
    i=0
    j=len(num)-1
    while i<j:
            num[i],num[j]=num[j],num[i]
            j=j-1
            i=i+1
    return num


print(leftrotate([10, 20, 30, 40, 50],2))

