def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]       

arr = [10,2,4,12,12,0]     
selectionSort(arr)   
print(arr,"Selection Sort")
