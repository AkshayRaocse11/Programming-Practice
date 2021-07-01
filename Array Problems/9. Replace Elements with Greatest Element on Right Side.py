# Replace Elements with Greatest Element on Right Side
def sort(arr):
    temp=[]
    n = len(arr)
    for i in range(n-1):
        temp =arr[i+1:]
        value = max(temp)
        arr[i]=value   
    arr[-1] = -1
    return arr
arr = arr = [17,18,5,4,6,1]

print(sort(arr),"Replace Elements with Greatest Element on Right Side")