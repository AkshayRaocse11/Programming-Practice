def countSort(arr):
    n= len(arr)
    max_ele = max(arr)
    count=[0]*(max_ele+1)
    result =[0]*n
    # store the count of each element of count array
    for i in range(n):
        count[arr[i]]+=1
    # store cumaltive sum of count array helps to find original array index value
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    # find index of each element of original array in count array and place the element in resultatn array
    i = n-1
    while i >=0:
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]]-=1
        i-=1
    arr = result
    return arr

arr = [10,20,90,1,2,3,5,100,10]
arr=countSort(arr)
print(arr,"Count Sort")
         

# Counting sort is a sorting technique based on keys between a specific range. 
# It works by counting the number of objects having distinct key values (kind of hashing). 
# Then doing some arithmetic to calculate the position of each object in the output sequence.
# Worst complexity: O(n+r) r - is auxiliary array
# Average complexity: (n+r)
# Space complexity: (n+r)
# Stable: Yes