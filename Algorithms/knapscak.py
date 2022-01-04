
# Python3 program to find minimum cost to
# get exactly W Kg with given packets
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    print(190//160)
    print(190%160)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# Driver code
val = [120 , 230, 450,774,1400,2800]
wt = [10, 20, 40,80,160,320]
W = 1150
n = len(val)    
print(knapSack(W, wt, val, n))
# Driver program to run the test case

   
