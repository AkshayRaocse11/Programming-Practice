def rotateArray(arr,k):
    n=len(arr)
    reverseArray(arr,n-k-1,n-k-1)
    reverseArray(arr,0,n-k-1)
    reverseArray(arr,0,n-1)
    return arr
def reverseArray(arr,start,end):
    i= start 
    j= end
    print(i,j,arr)
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr
arr = [1,2,3,4,5,6,7,8]
print(rotateArray(arr,k=3),"Rotate Right Array")
    

