# Increasing Triplet Subsequence Find Sorted Triplet in array

def sort(arr):
    j=1
    for i in range(len(arr)):
            if i<j and arr[i] < arr[j] < arr[j+1]:
                return [arr[i] , arr[j] , arr[j+1]]
arr = [1,5,2,7,3]
print(sort(arr),"Inversions in an array")