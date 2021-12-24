# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        count = 1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                count+=1
        if count >= 2:
            return True
        else:
            return False
        #return len(nums) != len(set(nums))

sol = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums))

