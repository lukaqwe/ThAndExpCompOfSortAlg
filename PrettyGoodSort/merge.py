def merge_sort(A):
    n = len(A)
    if(n < 2):
        return A
    mid = n/2
    left = []
    right = []
    for i in range(mid):
        number = A[i]
        left.append(number)
    for i in range(mid, n):
        number = A[i]
        right.append(number)
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)
    return A


def merge(left, right, A):
    i = j = k = 0
    while (i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k] = left[i]
            i = i+1
        else:
            A[k] = right[j]
            j = j+1
        k = k+1
    while(i < len(left)):
        A[k] = left[i]
        i = i+1
        k = k+1
    while(j < len(right)):
        A[k] = right[j]
        j = j+1
        k = k+1
