# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0 
        prev = 0   
        if len(A)  == 2:
            if A[0] == A[1]:
                return 0
            else:
                return 1
        
        for i in range(0,len(A)):
            # prev =  A[i]

            for j in range(i,len(A)):
                print(A[i:])
                if j %2:
                    odd = odd +A[j]
                else:
                    even = even +A[j]
            if odd == even:
                count = count+1



            
            # if copyArray:
            #     copyArray.pop(i)
            #     if copyArray[::2] and copyArray[1::2]:
            #         even=sum(copyArray[::2])
            #         odd=sum(copyArray[1::2])
            #         if even == odd:
            #             count = count+1
            #         # print(copyArray,"copyArray")
            #         # print(sum(copyArray[::2]),sum(copyArray[1::2]),copyArray,"copyArray")  
            # copyArray.insert(i,prev)

            # print(copyArray)
                 
        return count
sol = Solution()
A = [1,1,1]
print(sol.solve(A))