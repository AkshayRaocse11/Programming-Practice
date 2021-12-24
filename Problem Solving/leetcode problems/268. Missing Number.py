# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        x1,x2 = 0,0
        n = len(nums)
        for i in range(n + 1):
            x1^=i
        for i in nums:
            x2^=i
        return x1^x2

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(nums))

# return int((len(nums)*(len(nums)+1))/2-sum(nums)) solution 2