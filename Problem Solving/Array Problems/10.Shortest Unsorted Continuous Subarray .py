#Shortest Unsorted Continuous Subarray 
def sort(arr):
    stack = []
    start , end = len(arr),0
    #travese the array to from left to right
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            start = min(start,stack.pop())
            break
        stack.append(i)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] < arr[i]:
            end = max(end,stack.pop())
        stack.append(i)  
    if end - start > 0:
        return end-start+1
    else:
        return 0
arr = [2,6,4,8,10,9,15]
print(sort(arr),"Shortest Unsorted Continuous Subarray ")
            