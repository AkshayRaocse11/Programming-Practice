# https://leetcode.com/problems/majority-element/
class Solution:
	def majorityElement(self, votes: List[int]) -> int:
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
		candidate = 0

		#  # of majority - # of non-majority > 0
        # majority>n/2
        # [3,2,3] always 3 candiate will win majority of 3 occurs is 2 times .so highest votes are for candiate 3
		for vote in votes:
			# update majority
			if count ==0:
				candidate = vote

			if vote != candidate:
				count -=1
			else:
				count+=1
		return candidate