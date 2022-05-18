   #https://leetcode.com/problems/3sum/submissions/    
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(0,n-1):
            l = i+1
            r = n -1
            while l < r:
                cur_sum = nums [i] + nums [l] + nums [r]
                if cur_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif cur_sum < 0:
                    l+=1
                else:
                    r-=1
                    
        return set([tuple(x) for x in result])
            
#         for k in range(0,len(nums)):
#             i =0
#             j=1
#             sum =0
#             length = len(nums)
#             while j<len(nums)+1:
#                 sum = sum+1
#                 if sum == len(nums):
#                     if i!=j and i!=k and j!=k:
#                         result.append([nums[k],nums[i],nums[j]]) 
#                     break
#                 if nums[i] + nums[j] + nums[k] != 0 and i!=j!=k :
#                     j+=1
#                     if j == length:
#                         i+=1
#                         j=0
#                 else:
#                     if i!=j and i!=k and j!=k:
#                         if nums[i] + nums[j] + nums[k] == sum :
#                             result.append([nums[k],nums[i],nums[j]]) 
                        
        
        
 