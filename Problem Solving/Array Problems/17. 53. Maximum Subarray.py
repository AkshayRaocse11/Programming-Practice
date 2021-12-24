import sys
class Solution(object):
    def maxSubArray(self, nums):
        cur_sum=0
        max_val=-sys.maxsize-1
        for i in range(len(nums)):
            cur_sum=cur_sum+nums[i]
            if(max_val<cur_sum):
                max_val=cur_sum
            if(cur_sum<0):
                cur_sum=0
        return max_val
c = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = c.maxSubArray(nums)
print(" the element  ={}".format(test)) 