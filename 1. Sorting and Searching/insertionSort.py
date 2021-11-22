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

#Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
# The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked 
# and placed at the correct position in the sorted part.
#Time Complexity: O(n^2) 
#Auxiliary Space: O(1)
#Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
#    And it takes minimum time (Order of n) when elements are already sorted.
#Algorithmic Paradigm: Incremental Approach
#Sorting In Place: Yes
#Stable: Yes
        
    