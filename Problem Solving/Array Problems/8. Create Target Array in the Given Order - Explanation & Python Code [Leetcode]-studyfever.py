#16. Create Target Array in the Given Order - Explanation & Python Code [Leetcode]-studyfever
def sort(index,value):
    
    length = len(value)
    target = []
    for i in range(length):
        if index[i]>=length:
            target.append(value[i])
        else:
            target.insert(index[i],value[i])
    return target
valueArr = [1,4,3,5,6]
index = [3,1,3,3,2]
print(sort(index,valueArr))


    