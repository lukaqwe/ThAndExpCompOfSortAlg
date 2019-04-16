
def cocktail_sort(A):
    lenght = len(A)
    left, right = 0, lenght - 1

    while left <= right:
        for i in range(left, right, +1):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp

        right -= 1
        for i in range(right, left, -1):
            if A[i - 1] > A[i]:
                temp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = temp
        left += 1
    return A
