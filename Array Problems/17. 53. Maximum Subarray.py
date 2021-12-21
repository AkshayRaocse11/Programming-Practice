import sys
class Solution(object):
    def maxSubArray(self, arr):
        sum = 0
        max_ele = -sys.maxsize-1
        print(max_ele)
        n = len(arr)
        for i in range(1,n):
            sum = sum + arr[i]
            if(max_ele<sum):
                max_ele=sum            
            if max_ele < 0 :
                sum =0
        return sum
        
c = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = c.maxSubArray(nums)
print(" the element  ={}".format(test)) 