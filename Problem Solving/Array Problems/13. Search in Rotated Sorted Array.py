# 13. Search in Rotated Sorted Array
def find(arr,sum):
    arr.sort()
    n=len(arr)-1
    i = 0 
    while n > i:
        temp = arr[i]+arr[n]
        if temp == sum:
            return True
        if temp > sum:
            n-=1
        if temp < sum:
            i+=1
    return False
arr = [11,15,26,38,9,10]

print(find(arr,sum=11),"Search in Rotated Sorted Array")
