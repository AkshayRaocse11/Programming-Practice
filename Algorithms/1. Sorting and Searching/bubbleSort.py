def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                #swap 2 elements 
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr =[10,20,30,1,2,3,5]
bubbleSort(arr)
print(arr,"Bubble Sort")

# Bubble Sort is the simplest sorting algorithm that works 
# by repeatedly swapping the adjacent elements if they are in wrong order.
# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
# Auxiliary Space: O(1)