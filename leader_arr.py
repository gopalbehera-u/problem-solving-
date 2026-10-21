def leader(num):
    leaders = []
    max_iter=num[-1]
    leaders.append(max_iter)
    for i in range(len(num)-2,-1,-1):
        if max_iter <=num[i]:
            max_iter=num[i]
            leaders.append( max_iter)  
    i=0
    j=len(leaders)-1
    while i < j :
        leaders[i],leaders[j]=leaders[j],leaders[i]
        i+=1
        j-=1
    
    return leaders



print(leader([10, 8, 6, 7, 3]))