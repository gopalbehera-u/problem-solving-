


def movezeros(arr):
    i,j=0,0
    while j < len(arr):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        else:
            j+=1
    return arr[:i]


print(movezeros([0,5,0,3,8,9]))