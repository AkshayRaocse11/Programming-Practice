def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j       
        arr[i],arr[min] = arr[min],arr[i]
arr = [10,2,4,12,12,0]     
selectionSort(arr)   
print(arr,"Selection Sort")
