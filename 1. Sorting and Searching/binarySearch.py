def binarySearch(arr,s,e,k):
    if e >=s:
        mid = s +((e-s) //2)
        if arr[mid] == k:
            print(arr[mid])
            return k
        elif k < arr[mid]:
            binarySearch(arr,s,mid,k)
        elif k > arr[mid]:
            binarySearch(arr,mid+1,e,k)
    else:
        return -1

arr = [2,4,5,6,8,12,111,1]
k=111   
print(binarySearch(sorted(arr),0,(len(arr)-1),k))

    