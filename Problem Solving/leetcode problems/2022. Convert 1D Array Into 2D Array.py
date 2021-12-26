# https://leetcode.com/problems/convert-1d-array-into-2d-array/
class Solution(object):
    def construct2DArray(self, original, m, n):
        if m*n != len(original):
            return []
        temp = []
        for i in range(0, len(original), n):
            temp.append(original[i:i+n]) 
        return temp     

       

sol = Solution()
nums = [1,2,3,4,5,6]
m = 2
n = 3
print(sol.construct2DArray(nums, m, n))