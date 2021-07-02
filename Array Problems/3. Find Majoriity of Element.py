def countSort(arr):
    n = len(arr)
    max_ele = max(arr)
    count = [0]*(max_ele+1)
    seen = {}
    # store the count of each element of count array
    for i in range(n):
        count[arr[i]] += 1
        seen[arr[i]] = count[arr[i]]
    all_values = seen.values()
    max_value = max(all_values)
    for k, v in seen.items():
        if v == max_value:
            return k


arr = [1, 2, 2, 3]
print(countSort(arr), "Majority elements")
