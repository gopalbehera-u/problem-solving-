def twosum(num,target):
    for i in num:
        for j in num:
            if i+j==target:
                return True
    return False




print(twosum([2, 7, 11, 15],9))