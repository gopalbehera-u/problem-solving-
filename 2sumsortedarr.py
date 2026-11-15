def twosum(arr,target):
    left=0
    right=len(arr)-1
    while left <right:
        sum=arr[left]+arr[right]
        if sum <target:
            left+=1
        elif sum>target:
            right-=1
        else:
            return  [left+1, right+1]
    return []



numbers = [2, 17, 11, 15]
target = 9

print(twosum(numbers,target))