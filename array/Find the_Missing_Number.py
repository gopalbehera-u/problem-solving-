def findmissingnumber(num):
    n=len(num)+1
    expsum=n*((n+1)/2)
    actualsum=0
    for i in num:
        actualsum=actualsum+i

    return expsum-actualsum



print(findmissingnumber([1, 2, 3, 5]))