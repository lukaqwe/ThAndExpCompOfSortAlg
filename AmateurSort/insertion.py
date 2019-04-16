

def insertion_sort(A):
    n = len(A)
    if n == 1:
        return A
    for i in range(1, n):
        j = i
        while j != 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A
