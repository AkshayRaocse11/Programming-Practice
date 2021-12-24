# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]

sol = Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))
