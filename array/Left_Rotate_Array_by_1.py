def leftrotete(num):
    for i in range(len(num)-1):
        num[i],num[i+1]=num[i+1],num[i]
    return num


print(leftrotete([1, 2, 3, 4, 5]))