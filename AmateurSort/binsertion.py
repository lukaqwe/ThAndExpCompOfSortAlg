
def binary_search(A, el):
    n = len(A)
    low = 0
    up = len(A)-1
    while low < up:
        mid = (low + up)//2
        if A[mid] < el:
            low = mid+1
        elif A[mid] > el:
            up = mid-1
        else:
            return mid
    if low == up:
        if A[low] > el:
            return low
        return low+1
    return low


def binsertion_sort(A):
    for i in range(1, len(A)):
        val = A[i]
        j = binary_search(A[:i], val)
        A = A[:j] + [val] + A[j:i] + A[i+1:]
    return A
