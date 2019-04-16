
# stooge sort takes two arguments
# at the initial call left=0 and right=len(A)-1


def stooge_sort(A, left, right):
    if A[right] < A[left]:
        A[left], A[right] = A[right], A[left]
    if (right - left + 1) > 2:
        listPart = (right - left + 1) // 3
        stooge_sort(A, left, right - listPart)
        stooge_sort(A, left + listPart, right)
        stooge_sort(A, left, right - listPart)

    return A
