def countSort(arr,place):
    n= len(arr)
    count=[0]*(10)
    result =[0]*n
    # store the count of each element of count array
    for i in range(n):
        index = arr[i] // place
        count[index%10]+=1
    # store cumaltive sum of count array helps to find original array index value
    for i in range(1,10):
        count[i]+=count[i-1]
    # find index of each element of original array in count array and place the element in resultatn array
    i = n-1
    while i >=0:
        index = arr[i] // place
        result[count[index%10]-1] = arr[i]
        count[index%10]-=1
        i-=1
    for i in range(n):
        arr[i] = result[i]
def radixSort(arr):
    #find maximum elemnet in array
    max_ele =max(arr)
    #apply counting sort based on element places value
    place = 1
    while max_ele//place > 0 :
        countSort(arr,place)
        place*=10 
arr =[20000,200,9,12,4,5,6,1]        
radixSort(arr)
print(arr, "Quick sort")