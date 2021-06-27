def missingNumber(arr,n):
    x1,x2 = arr[0],1
    for i in range(1,n):
        x1^=arr[i]
    for i in range(2,n+2):
        x2^=i
    return x1^x2
arr = [1,2,3,5,7,6,8]
print(missingNumber(arr,len(arr)))
