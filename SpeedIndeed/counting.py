
def counting_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    range = max(A)-min(A) + 1
    # I created checkrange for this kind of situation A=[100..150] or A=[200..250] or A[300..305] etc.
    checkrange = min(A) - range
    counter = [0] * range
    for el in A:
        if checkrange < 0:
            counter[el-range] += 1
        else:
            counter[el-range-checkrange] += 1

    ndx = 0
    for i in xrange(range):
        while 0 < counter[i]:
            A[ndx] = i
            ndx += 1
            counter[i] -= 1
    return A
