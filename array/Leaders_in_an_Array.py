def leaderarr(num):
    largest=float('-inf')
    leader=[]
    for i in range(len(num)-1,-1,-1):
        if num[i] >largest:
            leader.append(num[i])
            largest=num[i]

    i=0 
    j=len(leader)-1
    while i<j:
        leader[i],leader[j]=leader[j],leader[i]
        i+=1
        j-=1

    return leader




print(leaderarr([]))