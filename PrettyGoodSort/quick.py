def partition(A, low, high):
    i = (low - 1)
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)


def quick_sort(A, low, high):  # at initial call low=0, high=len(A)-1
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi-1)
        quick_sort(A, pi+1, high)
    return A
