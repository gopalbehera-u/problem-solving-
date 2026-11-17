def revstr(stng):
    left=0
    right=len(stng)-1
    while left < right :
        stng[left],stng[right]=stng[right],stng[left]
        left+=1
        right-=1
    return stng




print(revstr(["H","a","n","n","a","h"]))





