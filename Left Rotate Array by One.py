def leftrotate(num):
    for i  in range(len(num)-1):
         num[i],num[i+1]=num[i+1],num[i]
    return num

print(leftrotate([1, 2, 3, 4, 5]))