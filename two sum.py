def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i, j]
    return []


print(twosum([5, 4, 16, 8], 12))