def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                #swap 2 elements 
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr =[10,20,30,1,2,3,5]
bubbleSort(arr)
print(arr,"Bubble Sort")

