# https://leetcode.com/problems/reshape-the-matrix/
class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # Check for validity of reshape
        if (m * n != r * c) or (m == r and n == c):
            return mat
        
        # Create output matrix
        out = []
        
        # Flatten the matrix
        M_flat = []
        for row in mat:
            M_flat += row
        print(M_flat)  
        # Populate rows with c elements taken sequentially from the flattened matrix, then add the row to the output matrix
        # Once complete the output matrix will have r rows consisting of c elements with the same row-traversing order as mat, as was desired
        while len(M_flat) > 0:
            row = []
            for i in range(c):
                x = M_flat.pop(0)
                row.append(x)
            out.append(row)
        
        return out 




sol = Solution()
nums = [[1,2],[3,4]]
m = 1
n = 4
print(sol.matrixReshape(nums, m, n))