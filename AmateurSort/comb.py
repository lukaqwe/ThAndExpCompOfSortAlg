
def comb_sort(A):
    lenght = len(A)
    gap = lenght * 10 // 13 if lenght > 1 else 0

    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = 0
        for index in range(lenght - gap):
            if A[index + gap] < A[index]:
                temp = A[index + gap]
                A[index + gap] = A[index]
                A[index] = temp
                swapped = 1
        gap = (gap * 10 // 13) or swapped

    return A
