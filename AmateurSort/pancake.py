

def reverse(A):
    return list(reversed(A))


def pancake_sort(A):
    i = 0
    while i != len(A)-1:
        mInd = A[i:].index(min(A[i:])) + i
        if mInd != i:
            A = A[:mInd] + reverse(A[mInd:])
            A = A[:i]+reverse(A[i:])
        i += 1
    return A
