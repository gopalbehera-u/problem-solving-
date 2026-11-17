def mergearrsorted(arr1,m,arr2,n):
    i=m-1
    j=n-1
    k=len(arr1)-1
    while i>=0 and j>=0:
        if arr1[i] <arr2[j]:
            arr1[k]=arr2[j]
            j-=1
        elif arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            i-=1
        else:
            arr1[k]=arr2[j]
            i-=1
            j-=1
        k-=1
    while j>=0:
        arr1[k]=arr2[j]
        j-=1
        k-=1
    
    return arr1





nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
m = 3
n = 3
print(mergearrsorted(nums1,m,nums2,n))
        
