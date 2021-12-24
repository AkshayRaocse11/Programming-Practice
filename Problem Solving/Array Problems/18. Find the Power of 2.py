class Solution(object):
    def isPowerOfTwo(self, n):
        rem,x2=0,2
        if n == 1:
            return True
        x2^=n
        if x2%2==0:
            return True
        else:
            return False
        
        
c = Solution()
n = c.isPowerOfTwo(16)
print(n)
#not completed