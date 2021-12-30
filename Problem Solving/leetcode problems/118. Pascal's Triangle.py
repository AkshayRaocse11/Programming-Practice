# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        p = [[1]]
        
        for i in range(1,numRows):
            lsf = []
            
            for j in range(0,len(p[i-1])-1):
                lsf.append(p[i-1][j]+p[i-1][j+1])
            
            p.append([1]+lsf+[1])
            
        return p       
           

sol = Solution()
numRows = 5
print(sol.generate(numRows))