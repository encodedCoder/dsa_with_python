def wave(A):
    A.sort()
    
    for i in range(0, len(A)-1, 2):
        A[i], A[i+1] = A[i+1], A[i]

    for i in range(len(A)):
        print(A[i], end=" ")

    print()


A = [ 5, 1, 3, 2, 4 ]
wave(A)
# print(A)