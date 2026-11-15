

def container_water(arr):
    left=0
    right=len(arr)-1
    max_area=0

    while left<right:
        area=(right-left)*min(arr[right],arr[left])
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1

        if area>max_area:
            max_area=area
    return max_area




print(container_water([3, 8, 5, 2, 7]))