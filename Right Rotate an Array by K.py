def rightrotate(num,k):
    if len(num)==0:
        return num
    k=k%len(num)
    j=len(num)-1
    i=0
    while i < j:
        num[i],num[j]=num[j],num[i]
        i+=1
        j-=1
    i=0
    j=k-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        i+=1
        j-=1
    i=k
    j=len(num)-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        i+=1
        j-=1
    

    return num
print([10,20,30,40,50])
print(rightrotate([10,20,30,40,50],7))