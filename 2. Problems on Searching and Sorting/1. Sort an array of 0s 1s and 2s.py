# https://leetcode.com/problems/sort-colors/submissions/
def dnf(nums):
    n = len(nums)
    C = 0
    L = 0
    H = n-1
    while C <= H:
        if nums[C] == 0:
            nums[L], nums[C] = nums[C], nums[L]
            L += 1
            C += 1
        elif nums[C] == 2:
            nums[C], nums[H] = nums[H], nums[C]
            H-=1
        else:
            C += 1
    return nums

arr = [0,1,0,1,2,2,1]
dnfV = dnf(arr)
print(dnfV)
