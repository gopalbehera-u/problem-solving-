def rotatekposition(num,k):
    if len(num)==0:
      return num
    k = k % len(num)
    i=0
    j=k-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        i=i+1
        j=j-1
    i=k
    j=len(num)-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        i=i+1
        j=j-1
    i=0
    j=len(num)-1
    while i<j:
        num[i],num[j]=num[j],num[i]
        i=i+1
        j=j-1
    return num



print('code')
print(rotatekposition([1, 2, 3, 4, 5],2))
print('code')