# 7. sort even first and odd last.py
def sortParity(arr):
    i=0
    j=(len(arr))-1
    while i < j:
        if arr[i]%2!=0:
            arr[i],arr[j] = arr[j],arr[i]
            j-=1  
        else:
            i+=1
    return arr

arr=[1,2,3,4,5,6]
print(sortParity(arr),"sorted array even first and odd second")

