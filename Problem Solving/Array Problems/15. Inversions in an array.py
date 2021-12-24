# 15. Inversions in an array
def mergeSort(arr):
    inversionCount = 0
    if len(arr)>1:
        mid = (len(arr))//2
        left = arr[:mid]
        right = arr[mid:] 
        mergeSort(left)
        mergeSort(right)
        inversionCount =  merge(arr,left,right)
    return inversionCount
def merge(arr,left,right):
    i = 0
    j =0 
    k = 0
    inversionCount = 0
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            inversionCount=len(left)-i
            arr[k] =right[j]
            j+=1
        k+=1      
    while i < len(left):
        arr[k] = left [i]
        i+=1
        k+=1
    while j<len(right)    :
        arr[k] = right[j]
        j+=1
        k+=1
    return inversionCount
"""def inversion(arr):
    inversionCount = 0
    arr.sort()
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if i< j and arr[i] > arr[j]:
                inversionCount+=1
    return inversionCount"""

arr = [2,5,1,7,9]
print(mergeSort(arr),"Inversions in an array")