#12 . Find Leaders in an array
def find(arr):
    leaders = []
    n = len(arr)
    for i in range(n-1):
        temp =arr[i+1:]
        value = max(temp)
        if arr[i]  > value:
            leaders.append(arr[i])
    return leaders
arr = [17,18,5,4,6,1]

print(find(arr),"Find Leaders in an array")
