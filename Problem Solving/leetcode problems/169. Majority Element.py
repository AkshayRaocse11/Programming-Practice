# https://leetcode.com/problems/majority-element/
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
#         # Solution1: Hashmap 
#         hashmap = dict()

#         for num in nums:
#             if num not in hashmap:
#                 hashmap[num] = 1
#             else:
#                 hashmap[num]+=1
#         for k,v in hashmap.items():
#             if v >= len(nums)/2:
#                 return k
#         return None


		# Solution2: Boyer-Moore Voting Algorithm
		count = 0
		res = 0

		#  # of majority - # of non-majority > 0
		for num in nums:
			# update majority
			if count ==0:
				res = num

			if num != res:
				count -=1
			else:
				count+=1
		return res