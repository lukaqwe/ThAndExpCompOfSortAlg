def pigeonhole_sort(A):

    range = max(A) - min(A) + 1
    holes = [0] * range

    # Populate the pigeonholes.
    for el in A:
        holes[el - min(A)] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in xrange(range):
        while holes[count] > 0:
            holes[count] -= 1
            A[i] = count + min(A)
            i += 1
    return A
