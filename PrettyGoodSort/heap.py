def heap_sort(A):
    # convert A to heap
    n = len(A) - 1
    leastParent = n / 2
    for i in range(leastParent, -1, -1):
        moveDown(A, i, n)

    # flatten heap into sorted array
    for i in range(n, 0, -1):
        if A[0] > A[i]:
            A[0], A[i] = A[i], A[0]
            moveDown(A, 0, i - 1)
    return A


def moveDown(A, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (A[largest] < A[largest + 1]):
            largest += 1

        # right child is larger than parent
        if A[largest] > A[first]:
            A[largest], A[first] = A[first], A[largest]
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return  # force exit
