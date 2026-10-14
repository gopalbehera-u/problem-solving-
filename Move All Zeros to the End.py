def movezeros(num):
    n=len(num)
    i=0
    j=0
    while i <n:
        if num[i]!=0:
            num[i],num[j]=num[j],num[i]
            j=j+1
        i=i+1
    return num



print(movezeros([0, 1, 0, 3, 12]))