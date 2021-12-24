# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        # result = []
        # cur = nums[0]
        # n = len(nums)
        # nums.sort()
        # for i in range(1,n):
        #     if nums[i-1] != i:
        #         result.append(i)
        #     cur = nums[i]
                

        # return result
        return  set(range(1, len(nums)+1))-set(nums)
        
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums))