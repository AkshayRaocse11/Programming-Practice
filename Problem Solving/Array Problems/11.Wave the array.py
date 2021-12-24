def wave(A):
    A = sorted(A)
    for i in range(0, len(A)-1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A
arr = [ 6, 17, 15, 13 ,19]
print(wave(arr),"Amazon","Adobe qUESTIONS")

    #def dummy(self, A):
		#A.sort()
		#j=1
		#for i in range(0, len(A), 2):
			#if j>=len(A):
				#return A
			#A[i] ,A[j]  = A[j],A[i]
			#j+=2
		#return A
