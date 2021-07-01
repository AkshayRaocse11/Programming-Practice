#5.Find number odd number based on its occurence
def findOdd(arr):
    count =[0]*(len(arr))
    countSet = {}
    for i in range(len(arr)):
        count[arr[i]] += 1
        countSet[arr[i]] = count[arr[i]]
    filteredOdd = []
    for k,v  in countSet.items():
        if  v%2 != 0 and v > 1:
            filteredOdd.append(k)
    return filteredOdd
def orderof1time(arr):
    ans = 0
    for i in range(len(arr)):
        ans =ans ^ arr[i]
    return ans


arr= [1,2,1,1,3,2,2,2,2,7,7,7]
print(findOdd(arr),"Odd Number is ,TC and SC O(n)")
print(orderof1time(arr),"Odd Number is, TC O(n), SC O(1)")