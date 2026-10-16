


def removeduplicate(num):
    # n=len(num)-1
    i=0
    j=1
    while j<len(num):
        if num[i] !=num[j]:
            num[i+1]=num[j]
            i=i+1
            
        j=j+1
    return num[:i+1]





print(removeduplicate( [1, 1, 2, 2, 3]))