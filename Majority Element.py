def mojorityelement (num):
    d={}
    n=len(num)/2
    for i in num:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for key in d:
        if d[key]>n:
            return key 
        else :
            return None


print(mojorityelement( [3, 3, 4, 3, 2, 3, 3]))