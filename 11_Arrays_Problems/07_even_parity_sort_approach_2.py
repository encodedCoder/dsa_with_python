# in-place approach i.e. O(1) space complexity 

def even_parity_sort(A):
    i = 0; j = len(A)-1
    while i < j:
        if A[i] % 2 == 1:
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return A


A = [3,1,2,4,5]
even_parity_sort(A)
print(A)