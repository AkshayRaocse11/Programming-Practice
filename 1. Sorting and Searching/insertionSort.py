# Program to sorting in ascending order using Insertion Sort.
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # key to sort
        j = i - 1  #previous value
        while j >= 0 and key < arr[j]:
            # Traversing sorted array, if found any value is less than key value , keep sorting
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key
       
arr = [ 9, 8, 7, 6, 4, 3, 2]
insertionSort(arr)
print(arr, "insertionSort array")


        
    