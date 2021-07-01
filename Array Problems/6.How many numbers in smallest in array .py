#6.How many numbers in smallest in array 
class Solution(object):
    def smallerNumbersThanCurrent( arr):
        count ={}
        for i,v in enumerate(sorted(arr)):
            if v not in count:
                count[v] = i
        return [count[v] for v in arr]
    arr = [1,2,3,6,5]
    print(smallerNumbersThanCurrent(arr),"count of smallest number")
    